from django.db import models
from django.conf import settings

# Create your models here.

class TriviaQuestion(models.Model):
    number = models.IntegerField(unique=True)
    text = models.TextField()
    attempted = models.IntegerField()
    correct = models.IntegerField()

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
        ordering = ['number']


class TriviaUserResponses(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    question = models.ForeignKey(TriviaQuestion)
    response = models.ForeignKey(TriviaChoices)

    def __str__(self):
        text = self.user.get_name() + "'s response to question " + str(self.question.number) + ": " + self.response
        return text
    
    class Meta:
        ordering = ['question.number']
        

class TriviaConversation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    entry = models.CharField(max_length=300)
    
    def __str__(self):
        return self.user.get_name() + ': ' + self.entry