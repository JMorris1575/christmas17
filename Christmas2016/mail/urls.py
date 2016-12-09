from django.conf.urls import url
from .views import (ManageEmail, SendInvitation, MailCompose, )

urlpatterns = [
    url(r'^$', ManageEmail.as_view()),
    url(r'^invitation/$', SendInvitation.as_view()),
    url(r'^compose/$', MailCompose.as_view()),
]
