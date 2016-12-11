from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import PermissionDenied

from question.models import Question, Response
from user.models import UserProfile
from user.decorators import class_login_required

import utils


@class_login_required
class QuestionList(View):
    pass


class CreateResponse(View):
    pass


class EditResponse(View):
    pass


class DeleteResponse(View):
    pass

