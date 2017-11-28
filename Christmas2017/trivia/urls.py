from django.conf.urls import url
from .views import (Scoreboard, DisplayQuestion, DisplayResult, )
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$',
        RedirectView.as_view(
        url='/trivia/scoreboard/')),
    url(r'^scoreboard/$',
        Scoreboard.as_view(),
        name='scoreboard'),
    ]
