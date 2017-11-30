from django.db import models
from django.conf import settings
from gifts.models import Gift

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    gift_selected = models.ForeignKey(Gift, null=True, blank=True)
    added_memories = models.BooleanField(default=False)
    trivia_questions_attempted = models.IntegerField()
    trivia_answers_correct = models.IntegerField()

    def __str__(self):
        return 'Profile for ' + self.user.get_full_name()

    def get_name(self):
        name = self.user.first_name
        if name == 'Brian':
            name += ' ' + self.user.last_name
        return name

