from django.conf.urls import url
from .views import (MemoryCreate, MemoryList,
                    MemoryEdit, MemoryDelete, )

urlpatterns = [
    url(r'^create/$', MemoryCreate.as_view()),
    url(r'^edit/$', MemoryList.as_view(), name="memory_list"),
    url(r'^(?P<memory_id>[0-9]+)/edit/$', MemoryEdit.as_view()),
    url(r'^(?P<memory_id>[0-9]+)/delete/$', MemoryDelete.as_view()),
]
