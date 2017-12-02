from django.contrib import admin
from .models import TriviaQuestion, TriviaChoices, TriviaUserResponse, TriviaConversation

# Register your models here.

admin.site.register(TriviaQuestion)
admin.site.register(TriviaChoices)
admin.site.register(TriviaUserResponse)
admin.site.register(TriviaConversation)
