from django.contrib import admin
from .models import TriviaQuestion, TriviaChoice, TriviaUserResponse, TriviaConversation

# Register your models here.

admin.site.register(TriviaQuestion)
admin.site.register(TriviaChoice)
admin.site.register(TriviaUserResponse)
admin.site.register(TriviaConversation)
