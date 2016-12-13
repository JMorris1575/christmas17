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
    template_name = 'question/response_create.html'

    def get(self, request, question_number=None):
        return render(request, self.template_name,
                      {'display_memory': utils.get_memory(),
                       'question': Question.objects.get(pk = question_number)})

    def post(self, request, question_number=None):
        current_question = Question.objects.get(pk=question_number)
        new_response = Response(question=current_question,
                              responder=request.user,
                              response=request.POST['response_text'])
        new_response.save()
        return redirect('question_list')




class EditResponse(View):
    pass


class DeleteResponse(View):
    pass

