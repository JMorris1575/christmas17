from django.conf.urls import url
from .views import (QuestionList, CreateResponse, EditResponse, DeleteResponse, )
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$',
        RedirectView.as_view(
            url='/question/list/')),
    url(r'^list/$', QuestionList.as_view(), name='question_list'),
    url(r'^(?P<question_number>[0-9]+)/response/create/$', CreateResponse.as_view(), name='create_response'),
    url(r'^(?P<question_number>[0-9]+)/response/(?P<response_number>[0-9]+)/$',
        RedirectView.as_view(url='edit/')),
    url(r'^(?P<question_number>[0-9]+)/response/(?P<response_number>[0-9]+)/edit/$',
        EditResponse.as_view(),
        name='edit_response'),
    url(r'^(?P<question_number>[0-9]+)/response/(?P<response_number>[0-9]+)/delete/$',
        DeleteResponse.as_view(),
        name='delete_response'),
]
