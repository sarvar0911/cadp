# from django import forms
# from .models import Question, Answer, AnswerChoice

# class AnswerAdminForm(forms.ModelForm):
#     class Meta:
#         model = Answer
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         if self.instance.pk and self.instance.question:
#             if self.instance.question.answer_type == Question.TEXT:
#                 self.fields.pop('choice', None)
#             else:
#                 self.fields.pop('text_response', None)
#                 self.fields['choice'].queryset = AnswerChoice.objects.filter(question=self.instance.question)
#         else:
#             self.fields['choice'].queryset = AnswerChoice.objects.none()
#             self.fields['text_response'].widget = forms.TextInput(attrs={'readonly': 'readonly'})

# class QuestionAdminForm(forms.ModelForm):
#     class Meta:
#         model = Question
#         fields = '__all__'
