from openpyxl import Workbook
from django.http import HttpResponse
# from django.utils.translation import gettext as _
from rest_framework.permissions import AllowAny
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import Poll, Question, Answer, Vote, Citizen
from users.models import CustomUser
from .serializers import CitizenSerializer, VoteSerializer, PollSerializer, PollDetailSerializer
from django.db import transaction
from rest_framework.pagination import PageNumberPagination


def process_votes(poll, votes):
    results = {
        "poll_title": poll.title,
        "results": []
    }

    citizen_data = {}

    for vote in votes:
        citizen = vote.citizen
        question = vote.question
        answer_options = [answer.options for answer in vote.selected_answers.all()]
        citizen_key = citizen.id

        if citizen_key not in citizen_data:
                    region_name = citizen.user.region.name if citizen.user.region else 'No Region'
                    citizen_data[citizen_key] = {
                        "poll_title": poll.title,
                        "citizen_name": f"{citizen.first_name} {citizen.last_name}",
                        "gender": citizen.gender,
                        "age": citizen.age,
                        "username": citizen.user.username,
                        "region": region_name,
                        "answers": {}
                    }


        if question.id not in citizen_data[citizen_key]["answers"]:
            citizen_data[citizen_key]["answers"][question.id] = []

        citizen_data[citizen_key]["answers"][question.id].extend(answer_options)

    for key, data in citizen_data.items():
        result_entry = {
            "citizen_name": data["citizen_name"],
            "gender": data["gender"],
            "age": data["age"],
            "username": data["username"],
            "region": data["region"],
            "questions": {qid: ', '.join(answers) for qid, answers in data["answers"].items()}
        }
        results["results"].append(result_entry)

    return results


class ExportPollResultsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        try:
            wb = Workbook()
            ws = wb.active
            ws.title = "Poll Results"

            headers = [
                "Poll Title", "Citizen Name", "Gender", "Age", 
                "Username", "Region"
            ]

            polls = Poll.objects.prefetch_related(
                'questions__answers',
                'questions__votes__citizen__user'
            ).all()

            max_questions = max(poll.questions.count() for poll in polls)

            for i in range(1, max_questions + 1):
                headers.append(f"Q{i}")

            ws.append(headers)

            for poll in polls:
                votes = Vote.objects.filter(question__poll=poll).select_related('citizen', 'question').prefetch_related('selected_answers', 'citizen__user')
                results = process_votes(poll, votes)

                for data in results["results"]:
                    row = [
                        results["poll_title"],
                        data["citizen_name"],
                        data["gender"],
                        data["age"],
                        data["username"],
                        data["region"]
                    ]

                    for qid in range(1, max_questions + 1):
                        row.append(data["questions"].get(qid, ''))

                    ws.append(row)

            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="poll_results.xlsx"'
            wb.save(response)

            return response
        except Exception as e:
            return HttpResponse(f'Error generating Excel file: {str(e)}', status=500)

        
class PollResultsView(APIView):
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['citizen__gender', 'citizen__age', 'citizen__user__region']

    def get(self, request, poll_id):
        try:
            poll = Poll.objects.get(id=poll_id)
            votes = Vote.objects.filter(question__poll=poll)\
                .select_related('citizen__user__region', 'question')\
                .prefetch_related('selected_answers')

            for backend in list(self.filter_backends):
                votes = backend().filter_queryset(request, votes, self)

            results = process_votes(poll, votes)
            filtered_results = results["results"]

            paginator = PageNumberPagination()
            paginated_results = paginator.paginate_queryset(filtered_results, request)
            return paginator.get_paginated_response({
                "poll_title": results["poll_title"],
                "results": paginated_results
            })
        except Poll.DoesNotExist:
            return Response({'error': 'Poll not found.'}, status=status.HTTP_404_NOT_FOUND)


class VoteCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = VoteSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            try:
                with transaction.atomic():
                    response_data = serializer.save()
                    return Response({'success': 'Votes recorded successfully.', 'data': response_data}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PollListView(generics.ListCreateAPIView):
    queryset = Poll.objects.prefetch_related('questions')
    serializer_class = PollSerializer


class PollDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.prefetch_related('questions__answers')
    serializer_class = PollDetailSerializer


class VoteListView(generics.ListAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
