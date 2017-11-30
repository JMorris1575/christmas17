from django.contrib import admin
from .models import TriviaQuestion, TriviaChoices, TriviaUserResponses, TriviaConversation

# Register your models here.

admin.site.register(TriviaQuestion)
admin.site.register(TriviaChoices)
admin.site.register(TriviaUserResponses)
admin.site.register(TriviaConversation)
