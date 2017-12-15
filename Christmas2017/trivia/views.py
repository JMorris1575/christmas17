from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View, ListView, DetailView
from django.http import HttpResponseRedirect

from .models import TriviaQuestion, TriviaChoice, TriviaUserResponse
from django.contrib.auth.models import User
from user.models import UserProfile

from operator import itemgetter

import utils


# Create your views here.


class Scoreboard(View):
    template_name = 'trivia/scoreboard.html'

    def get(self, request):
        stats = self.stats()
        return render(request, self.template_name, {'display_memory': utils.get_memory(),
                                                    'stats':stats})

    def stats(self):
        users = UserProfile.objects.all()
        temp = []
        for user in users:
            attempts = user.trivia_questions_attempted
            correct = user.trivia_answers_correct
            if attempts != 0:
                percent = '{:.1%}'.format(correct/attempts)
            else:
                percent = '0.0%'
            name = user.get_name()
            if attempts > 0:
                temp.append( {'attempts':attempts, 'correct':correct, 'percent':percent, 'name':name} )
        temp_sorted = sorted(temp, key = itemgetter('attempts', 'correct'), reverse=True)
        stats = []
        attempt_group = -1
        for stat in temp_sorted:
            if stat['attempts'] == attempt_group:
                stats.append(dict(type='stat', value=stat))
            else:
                print('Got here')
                attempt_group = stat['attempts']
                stats.append(dict(type='heading', value='Players attempting ' + str(attempt_group) + ' questions:'))
                stats.append(dict(type='stat', value=stat))
        return stats



class DisplayQuestion(View):
    template_name = 'trivia/trivia_question.html'

    def get(self, request, question_number=None, error_message=None):
        if int(question_number) > request.user.userprofile.get_next_trivia():  # prevents going beyond the next question
            question_number = request.user.userprofile.get_next_trivia()
            return redirect('/trivia/question/' + str(question_number) + '/')
        if int(question_number) > len(TriviaQuestion.objects.all()):
            return redirect(reverse('end_of_questions'))
        question = TriviaQuestion.objects.get(number=question_number)
        choices = TriviaChoice.objects.filter(question=question.pk)
        return render(request, self.template_name, {'display_memory': utils.get_memory(),
                                                    'question': question,
                                                    'choices': choices,
                                                    'error_message':error_message})


class DisplayResult(View):
    template_name = 'trivia/trivia_result.html'

    def get(self, request, question_number=None, choice_number=None):
        question = TriviaQuestion.objects.get(number=question_number)
        user_choice = TriviaChoice.objects.filter(question=question).get(number=choice_number)
        correct_choice = TriviaChoice.objects.filter(question=question).get(correct=True)
        return render(request, self.template_name, {'display_memory': utils.get_memory(),
                                                    'question': question,
                                                    'user_choice': user_choice,
                                                    'correct_choice': correct_choice})


class EndOfQuestions(View):
    template_name = 'trivia/end_of_ques.html'

    def get(self, request):
        return render(request, self.template_name, {'display_memory': utils.get_memory(),})


class AlreadyAnswered(View):
    template_name = 'trivia/already_answered.html'

    def get(self, request):
        return render(request, self.template_name, {'display_memory': utils.get_memory(),})


class QuestionList(ListView):
    template_name = 'trivia/trivia_list.html'
    model = TriviaQuestion

    def get_context_data(self, **kwargs):
        context = super(QuestionList, self).get_context_data(**kwargs)
        context['display_memory'] = utils.get_memory()
        return context


class TriviaEdit(View):
    template_name = 'trivia/trivia_edit.html'

    def get(self, request):
        question_numbers = request.GET.getlist('trivia_questions')
        for question_number in question_numbers:

            return render(request, self.template_name)

    def post(self, request):
        print('Got to the post method of TriviaEdit')
        return redirect('gift_list')

def trivia_list_edit(request):
    question_numbers = request.GET.getlist('trivia_questions')
    for number in question_numbers:
        question = TriviaQuestion.objects.get(number=number)
        choices = TriviaChoice.objects.filter(question=question.pk)
    return render(request, 'trivia/trivia_edit.html', {'question': question,
                                                       'choices': choices,
                                                       'display_memory': utils.get_memory(),})


class ComposeTrivia(View):
    template_name = 'trivia/trivia_compose.html'

    def get(self, request):
        return render(request, self.template_name, {'display_memory': utils.get_memory(),})


class TemporarilyClosed(View):
    template_name = 'trivia/temporarily_closed.html'

    def get(self, request):
        return render(request, self.template_name, {'display_memory': utils.get_memory(),})


def trivia_choice(request, question_number=None):
    if int(question_number) < request.user.userprofile.get_next_trivia():
        return redirect(reverse('already_answered'))
    question = TriviaQuestion.objects.get(number=question_number)
    choices = TriviaChoice.objects.filter(question=question.pk)
    try:
        choice_index = request.POST['choice']
    except (KeyError, TriviaChoice.DoesNotExist):
        return render(request, 'trivia/trivia_question.html',
                      {'question': question,
                       'choices': choices,
                       'display_memory': utils.get_memory(),
                       'error_message': 'You must choose one of the responses below.'})
    else:
        choice = TriviaChoice.objects.filter(question=question).get(number=choice_index)
        user_response = TriviaUserResponse(user=request.user, question=question, response=choice)
        user_response.save()
        profile = request.user.userprofile
        profile.trivia_questions_attempted += 1
        if choice.correct:
            profile.trivia_answers_correct += 1
        profile.save()
        return redirect('trivia_result', question_number=question_number, choice_number=choice.number)
