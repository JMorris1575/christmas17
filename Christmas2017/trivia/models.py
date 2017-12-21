from django.db import models
from django.conf import settings
from django.urls import reverse

import utils

# Create your models here.

class TriviaQuestion(models.Model):
    number = models.IntegerField(unique=True)
    text = models.TextField()
    attempted = models.IntegerField(default=0)
    correct = models.IntegerField(default=0)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['number']

    def get_choices(self):
        return TriviaChoice.objects.filter(question=self)

    def count(self):
        return len(TriviaQuestion.objects.all())

    def get_absolute_url(self):
        return reverse('trivia_edit', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('question_edit', kwargs={'pk': self.pk})


class TriviaChoice(models.Model):
    question = models.ForeignKey(TriviaQuestion)
    number = models.IntegerField()
    text = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
    
    class Meta:
        unique_together = ('question', 'number')
        ordering = ['question', 'number']

    def index(self):
        return ' ' + chr(64 + self.number) + ') '

    def get_absolute_url(self):
        return reverse('trivia_edit', kwargs={'pk': self.question.pk})

    def get_update_url(self):
        return reverse('choice_edit', kwargs={'pk': self.pk})


class TriviaUserResponse(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    question = models.ForeignKey(TriviaQuestion)
    response = models.ForeignKey(TriviaChoice)

    def __str__(self):
        text = self.user.userprofile.get_name() + "'s response to question " + \
               str(self.question.number) + ": " + str(self.response)
        return text
    
    class Meta:
        ordering = ['question']
        

class TriviaConversation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    entry = models.CharField(max_length=300)
    
    def __str__(self):
        return self.user.userprofile.get_name() + ': ' + self.entry