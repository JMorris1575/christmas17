from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView
from django.urls import reverse
from .views import (Scoreboard, DisplayQuestion, DisplayResult, )

urlpatterns = [
    url(r'^$',
        RedirectView.as_view(
        url='/trivia/scoreboard/')),
    url(r'^scoreboard/$',
        login_required(Scoreboard.as_view()),
        name='scoreboard'),
    url(r'^question/$',
        RedirectView.as_view(pattern_name='scoreboard')),
    url(r'^question/(?P<question_number>[0-9]+)/$',
        login_required(DisplayQuestion.as_view()),
        name='display_question'),
    url(r'^result/$',
        RedirectView.as_view(pattern_name='scoreboard')),
    url(r'^result/(?P<question_number>[0-9]+)/$',
        login_required(DisplayResult.as_view()),
        name='display_result'),
]