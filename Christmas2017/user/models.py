from django.db import models
from django.conf import settings
from gifts.models import Gift

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    gift_selected = models.ForeignKey(Gift, null=True, blank=True)
    added_memories = models.BooleanField(default=False)
    trivia_questions_attempted = models.IntegerField(default=0)
    trivia_answers_correct = models.IntegerField(default=0)

    def __str__(self):
        return 'Profile for ' + self.user.get_full_name()

    def get_name(self):
        name = self.user.first_name
        if name == 'Brian':
            name += ' ' + self.user.last_name
        return name

    def get_next_trivia(self):
        next_ques = self.trivia_questions_attempted + 1
        return next_ques

    def score(self):
        return '{:.1%}'.format(self.trivia_answers_correct / self.trivia_questions_attempted)


