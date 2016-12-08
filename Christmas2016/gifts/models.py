import os

from django.db import models
from django.conf import settings

from model_mixins import AuthorMixin as AuthorMixin

class Gift(models.Model):
    gift_number = models.IntegerField()
    description = models.TextField()
    wrapped = models.BooleanField(default=True)
    selected = models.BooleanField(default=False)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    receiver_name = models.CharField(max_length=10, blank=True)

    class Meta:
        ordering = ['gift_number']

    def __str__(self):
        return 'Gift ' + str(self.gift_number)

    def get_image_filename(self):
        if self.wrapped:
            status = 'wrapped'
        else:
            status = 'unwrapped'
        return os.path.join('gifts', 'images', status,
                            'Gift ' + str(self.gift_number) + '.png')

    def get_thumbnail_filename(self):
        if self.wrapped:
            status = 'wrapped'
        else:
            status = 'unwrapped'
        print(os.path.join('gifts', 'images', status, 'thumbnails',
                           'Gift ' + str(self.gift_number) + '.png'))
        return os.path.join('gifts', 'images', status, 'thumbnails',
                            'Gift ' + str(self.gift_number) + '.png')


    def get_comments(self):
        comments = Comment.objects.filter(gift=self)
        return comments


class Comment(models.Model, AuthorMixin):
    gift = models.ForeignKey(Gift)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    comment = models.TextField()

    def __str__(self):
        if len(self.comment) > 10:
            return self.comment[0:9] + '...'
        else:
            return self.comment

    def display(self):
        prefix = self.author() + ' says: '
        return prefix + self.comment

