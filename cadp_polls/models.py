from django.db import models
from django.conf import settings


class Citizen(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username}'


class Poll(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    questions_count = models.PositiveIntegerField(default=0)
    participants_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Question(models.Model):
    SINGLE_CHOICE = 'single_choice'
    MULTIPLE_CHOICE = 'multiple_choice'
    
    ANSWER_TYPES = [
        (SINGLE_CHOICE, 'Single Choice'),
        (MULTIPLE_CHOICE, 'Multiple Choice'),
    ]
    
    poll = models.ForeignKey(Poll, related_name='questions', on_delete=models.CASCADE)
    question_text = models.TextField()
    question_type = models.CharField(max_length=20, choices=ANSWER_TYPES, default=SINGLE_CHOICE)

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.CharField(max_length=255)
    options = models.CharField(max_length=2, null=True, blank=True) 

    def __str__(self):
        return self.answer_text


class Vote(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='votes')
    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE, related_name='votes')
    selected_answers = models.ManyToManyField(Answer, blank=True)

    def __str__(self):
        return f"Vote for '{self.question}' by {self.citizen}"
