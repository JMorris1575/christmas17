from django.conf.urls import url
from .views import (GiftList, SingleGift, Select, ChangeMind,
                    AddComment, EditComment, DeleteComment, )
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$',
        RedirectView.as_view(
        url='/gift/list/')),
    url(r'^list/$',
        GiftList.as_view(),
        name='gift_list'),
    url(r'^select/$', Select.as_view()),
    url(r'^change_mind/$', ChangeMind.as_view()),
    url(r'^(?P<giftNumber>[0-9]+)/$', SingleGift.as_view()),
    url(r'^(?P<gift_number>[0-9]+)/comment/$', AddComment.as_view()),
    url(r'^(?P<gift_number>[0-9]+)/comment/(?P<comment_number>[0-9]+)/$',
        RedirectView.as_view(url='edit/')),
    url(r'^(?P<gift_number>[0-9]+)/comment/(?P<comment_number>[0-9]+)/edit/$', EditComment.as_view()),
    url(r'^(?P<gift_number>[0-9]+)/comment/(?P<comment_number>[0-9]+)/delete/$', DeleteComment.as_view())
]
