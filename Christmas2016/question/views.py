from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import PermissionDenied

from question.models import Question, Response
from user.models import UserProfile
from user.decorators import class_login_required

import utils, datetime


@class_login_required
class QuestionList(View):
    template_name = 'question/question_list.html'

    def get(self, request):
        return render(request, self.template_name,
                      {'display_memory': utils.get_memory(),
                       'question_list': Question.objects.filter(date__lte=datetime.date.today()).order_by('-date'),
                       })



class CreateResponse(View):
    pass


class EditResponse(View):
    pass


class DeleteResponse(View):
    pass

