from django.db import models

class EmailTemplate(models.Model):
    name = models.CharField(max_length=15, blank=False)
    template = models.TextField()

    def __str__(self):
        return self.name

