from django.contrib import admin
from .models import Poll, Question, Answer, Vote, Citizen

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1
    inlines = [AnswerInline]  # Nest AnswerInline here

class PollAdmin(admin.ModelAdmin):
    exclude = ['questions_count', 'participants_count']
    inlines = [QuestionInline]

admin.site.register(Poll, PollAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Vote)
admin.site.register(Citizen)
