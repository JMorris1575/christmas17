from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import PermissionDenied

from story.models import Story
from user.models import UserProfile
from user.decorators import class_login_required

import utils


@class_login_required
class StoryDisplay(View):
    template_name = 'story/story.html'

    def get(self, request):
        return render(request, self.template_name,
                      { 'display_memory': utils.get_memory })


@class_login_required
class StoryAdd(View):
    template_name = 'story/story_add.html'

    def get(self, request):
        return render(request, self.template_name,
                      { 'display_memory': utils.get_memory})

    def post(self, request):
        # add to database
        return redirect('display_story')


@class_login_required
class StoryEdit(View):
    template_name = 'story/story_edit.html'

    def get(self, request, entry_number=None):
        return render(request, self.template_name,
                      {'entry_number': entry_number,
                       'display_memory': utils.get_memory})

    def post(self, request, entry_number=None):
        # make changes in database if this is the right user
        return redirect('display_story')