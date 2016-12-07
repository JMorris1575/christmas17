from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import RedirectView

from .views import LoginError


urlpatterns = [
    url(r'^$',
        RedirectView.as_view(
            pattern_name='dj-auth:login',
            permanent=False)),
    url(r'^login/$',
        auth_views.login,
        {'template_name': 'user/login_error.html',
         'redirect_authenticated_user': True },
        name='login'),
    url(r'login/error/$',
        LoginError.as_view()),
    url(r'^logout/$',
        auth_views.logout,
        {'template_name': 'user/login.html',
         'extra_context': {'form': AuthenticationForm}},
        name='logout'),
]