from rest_framework import serializers
from .models import Poll, Question, Answer, Vote, Citizen
from django.db import transaction


class CitizenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citizen
        fields = ['first_name', 'last_name', 'gender', 'age']


class VoteDetailSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    answer_ids = serializers.ListField(child=serializers.IntegerField())

    def validate(self, data):
        question_id = data['question_id']
        answer_ids = data['answer_ids']

        question = Question.objects.filter(id=question_id).first()
        if not question:
            raise serializers.ValidationError(f"Question with id {question_id} does not exist.")

        answers = Answer.objects.filter(id__in=answer_ids, question=question)
        if answers.count() != len(answer_ids):
            raise serializers.ValidationError("Some answer IDs do not match the question or do not exist.")

        if question.question_type == Question.SINGLE_CHOICE and len(answers) != 1:
            raise serializers.ValidationError("Single choice question must have exactly one answer selected.")
        
        if question.question_type == Question.MULTIPLE_CHOICE and len(answers) < 1:
            raise serializers.ValidationError("At least one answer must be selected for multiple choice question.")

        return data


class VoteSerializer(serializers.Serializer):
    citizen = CitizenSerializer()
    question = VoteDetailSerializer(many=True)

    def create(self, validated_data):
        citizen_data = validated_data.get('citizen')
        question_data = validated_data.get('question')

        request = self.context.get('request')
        user = request.user
        with transaction.atomic():            
            citizen = Citizen.objects.create(
                user=user,
                **citizen_data
            )

        response_data = {'citizen_username': citizen.user.username, 'questions': []}

        question_ids = [q_data['question_id'] for q_data in question_data]
        questions = {q.id: q for q in Question.objects.select_related('poll').filter(id__in=question_ids)}

        votes = []
        for q_data in question_data:
            question = questions[q_data['question_id']]
            answer_ids = q_data.get('answer_ids', [])
            selected_answers = Answer.objects.filter(id__in=answer_ids, question=question)

            vote = Vote(question=question, citizen=citizen)
            votes.append(vote)
            response_data['questions'].append({
                'question_text': question.question_text,
                'selected_answers': [answer.answer_text for answer in selected_answers]
            })

        Vote.objects.bulk_create(votes)

        for vote, q_data in zip(votes, question_data):
            answer_ids = q_data.get('answer_ids', [])
            selected_answers = Answer.objects.filter(id__in=answer_ids, question=vote.question)
            vote.selected_answers.set(selected_answers)

        return response_data


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'answer_text', 'options']


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'question_type', 'answers']

    def get_queryset(self):
        return super().get_queryset().prefetch_related('answers')


class PollSerializer(serializers.ModelSerializer):
    questions_count = serializers.ReadOnlyField()
    participants_count = serializers.ReadOnlyField()

    class Meta:
        model = Poll
        fields = ['id', 'title', 'description', 'questions_count', 'participants_count']


class PollDetailSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    questions_count = serializers.ReadOnlyField()
    participants_count = serializers.ReadOnlyField()

    class Meta:
        model = Poll
        fields = ['id', 'title', 'description',
                  'questions', 'questions_count',
                  'participants_count']

    def get_queryset(self):
        return super().get_queryset().prefetch_related('questions__answers')
