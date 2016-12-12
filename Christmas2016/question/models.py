from django.db import models
from django.conf import settings

from model_mixins import AuthorMixin as AuthorMixin


class Question(models.Model):
    question = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.question

    def get_responses(self):
        return Response.objects.filter(question=self)

    def get_responders(self):
        responses = self.get_responses()
        responders = []
        for response in responses:
            responders.append(response.responder)
        return responders


class Response(models.Model, AuthorMixin):
    response = models.TextField()
    question = models.ForeignKey(Question)
    responder = models.ForeignKey(settings.AUTH_USER_MODEL)
    entered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.response

    def display(self):
        prefix = self.author(self.responder) + " says: "
        return prefix + self.response