from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView
from django.urls import reverse
from .views import (Scoreboard, DisplayQuestion, DisplayResult,
                    EndOfQuestions, AlreadyAnswered, ComposeTrivia,
                    QuestionList, TriviaEdit, TemporarilyClosed,
                    QuestionEdit, ChoiceEdit,
                    trivia_choice, trivia_list_edit)

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
    url(r'^process_choice/(?P<question_number>[0-9]+)/$',
        trivia_choice, name='trivia_submit'),
    url(r'^result/$',
        RedirectView.as_view(pattern_name='scoreboard')),
    url(r'^result/(?P<question_number>[0-9]+)/(?P<choice_number>[0-9]+)/$',
        login_required(DisplayResult.as_view()),
        name='trivia_result'),
    url(r'^no_more_questions/$', login_required(EndOfQuestions.as_view()), name='end_of_questions'),
    url(r'^already_answered/$', login_required(AlreadyAnswered.as_view()), name='already_answered'),
    url(r'^list/$', QuestionList.as_view(), name='question_list'),
    url(r'^edit/$', trivia_list_edit, name='trivia_edit'),
    url(r'^edit/question/(?P<pk>\d+)/$', QuestionEdit.as_view(), name='question_edit'),
    url(r'edit/choice/(?P<pk>\d+)/$', ChoiceEdit.as_view(), name='choice_edit'),
    url(r'^compose/$', login_required(ComposeTrivia.as_view())),
    url(r'^temporarily_closed/$', login_required(TemporarilyClosed.as_view()), name='temporarily_closed',)
]
