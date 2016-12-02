from django.conf.urls import url
from .views import (ManageEmail, SendInvitation, MailCompose, MailManageTrade, )

urlpatterns = [
    url(r'^$', ManageEmail.as_view()),
    url(r'^invitation/$', SendInvitation.as_view()),
    url(r'^compose/$', MailCompose.as_view()),
    url(r'^trade/$', MailManageTrade.as_view()),
]
