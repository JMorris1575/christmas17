from django.db import models
from django.conf import settings

from model_mixins import AuthorMixin as AuthorMixin


class Story(models.Model, AuthorMixin):
    entry = models.TextField()
    entry_number = models.IntegerField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    publish_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.entry

