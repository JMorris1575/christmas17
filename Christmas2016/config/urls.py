"""Christmas2016 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('user.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^gift/', include('gifts.urls')),
    url(r'^memory/', include('memory.urls')),
    url(r'^mail/', include('mail.urls')),
    url(r'^user/',
        include('user.urls',
                app_name='user',
                namespace='dj-auth')),
    url(r'^story/', include('story.urls')),
    url(r'^question/', include('question.urls')),
]

admin.site.site_header = 'Christmas 2016 Admin'
admin.site.site_title = 'C-2016 Site Admin'
