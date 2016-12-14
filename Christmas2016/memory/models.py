from django.db import models
from django.conf import settings

from model_mixins import AuthorMixin as AuthorMixin


class Memory(models.Model, AuthorMixin):
    post = models.TextField(max_length=400)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.post

    def author_display(self):
        return 'Christmas Memory from ' + self.author(self.user) + ": "

