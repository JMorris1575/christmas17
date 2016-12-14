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
        try:
            question = Question.objects.get(pk=question_number)
        except:
            return redirect('question_list')
        return render(request, self.template_name,
                      {'display_memory': utils.get_memory(),
                       'question': question})

    def post(self, request, question_number=None):
        try:
            current_question = Question.objects.get(pk=question_number)
        except:
            return redirect('question_list')
        new_response = Response(question=current_question,
                              responder=request.user,
                              response=request.POST['response_text'])
        new_response.save()
        return redirect('question_list')


class EditResponse(View):
    template_name = 'question/response_edit.html'

    def get(self, request, question_number=None, user_id=None):
        try:
            current_question = Question.objects.get(pk=question_number)
            response = Response.objects.get(question=current_question, responder=user_id)
        except:
            return redirect('question_list')
        if request.user == response.responder:
            return render(request, self.template_name,
                          {'display_memory': utils.get_memory(),
                           'question': current_question,
                           'response': response})
        else:
            raise PermissionDenied

    def post(self, request, question_number=None, user_id=None):
        try:
            current_question = Question.objects.get(pk=question_number)
            response = Response.objects.get(question=current_question, responder=user_id)
        except:
            return redirect('question_list')
        if request.user == response.responder:
            response.response = request.POST['response_text']
            response.save()
            return redirect('question_list')
        else:
            raise PermissionDenied


class DeleteResponse(View):
    template_name = 'question/response_delete.html'

    def get(self, request, question_number=None, user_id=None):
        try:
            current_question = Question.objects.get(pk=question_number)
            response = Response.objects.get(question=current_question, responder=user_id)
        except:
            return redirect('question_list')
        if request.user == response.responder:
            return render(request, self.template_name,
                          {'display_memory': utils.get_memory(),
                           'question': current_question,
                           'response': response}
                          )
        else:
            raise PermissionDenied

    def post(self, request, question_number=None, user_id=None):
        try:
            current_question = Question.objects.get(pk=question_number)
            response = Response.objects.get(question=current_question, responder=user_id)
        except:
            return redirect('question_list')
        if request.user == response.responder:
            response.delete()
            return redirect('question_list')
        else:
            raise PermissionDenied

