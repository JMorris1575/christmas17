from django.db import models
from django.conf import settings

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


class TriviaChoices(models.Model):
    question = models.ForeignKey(TriviaQuestion)
    number = models.IntegerField()
    text = models.CharField(max_length=60)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
    
    class Meta:
        unique_together = ('question', 'number')
        ordering = ['question', 'number']

    def index(self):
        return ' ' + chr(64 + self.number) + ') '


class TriviaUserResponse(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    question = models.ForeignKey(TriviaQuestion)
    response = models.ForeignKey(TriviaChoices)

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