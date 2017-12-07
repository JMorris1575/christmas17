from django.conf.urls import url
from django.views.generic import RedirectView
from .views import (UnderConstruction)

urlpatterns = [
    url(r'^$', UnderConstruction.as_view(), name='under_construction'),
]