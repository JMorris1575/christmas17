from django.conf.urls import url
from .views import (StoryDisplay, StoryAdd, StoryEdit)
# from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$', StoryDisplay.as_view(), name='display_story' ),
    url(r'^add/$', StoryAdd.as_view(), name='story_add'),
    url(r'^(?P<entry_number>[0-9]+)/edit/$', StoryEdit.as_view()),
    # maybe add story delete for entries that have not yet had a successor
]
