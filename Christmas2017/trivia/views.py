from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View

from .models import TriviaQuestion, TriviaChoices, TriviaUserResponse
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
        print('stats = ',stats)
        return stats



class DisplayQuestion(View):
    template_name = 'trivia/trivia_question.html'

    def get(self, request, question_number=None):
        if int(question_number) > request.user.userprofile.get_next_trivia():    # prevents going beyond the next question
            question_number = request.user.userprofile.get_next_trivia()
            return redirect('/trivia/question/' + str(question_number) + '/')
        if int(question_number) > len(TriviaQuestion.objects.all()):
            return redirect(reverse('end_of_questions'))
        question = TriviaQuestion.objects.get(number=question_number)
        choices = TriviaChoices.objects.filter(question=question.pk)
        return render(request, self.template_name, {'display_memory': utils.get_memory(),
                                                    'question': question,
                                                    'choices': choices})


class DisplayResult(View):
    template_name = 'trivia/trivia_result.html'

    def get(self, request, question_number=None):
        return render(request, self.template_name, {'display_memory': utils.get_memory(),
                                                    'q_number': question_number})

    def post(self, request, question_number=None):
        if int(question_number) < request.user.userprofile.get_next_trivia():
            return redirect(reverse('already_answered'))
        choice_index = request.POST['choice']
        question = TriviaQuestion.objects.get(number=question_number)
        choice = TriviaChoices.objects.filter(question=question).get(number=choice_index)
        correct_choice = TriviaChoices.objects.filter(question=question).get(correct=True)
        user_response = TriviaUserResponse(user=request.user, question=question, response=choice)
        user_response.save()
        profile = request.user.userprofile
        profile.trivia_questions_attempted += 1
        if choice.correct:
            profile.trivia_answers_correct += 1
        profile.save()

        return render(request, self.template_name, {'display_memory': utils.get_memory(),
                                                    'question': question,
                                                    'choice': choice,
                                                    'correct_choice': correct_choice})


class EndOfQuestions(View):
    template_name = 'trivia/end_of_ques.html'

    def get(self, request):
        return render(request, self.template_name, {'display_memory': utils.get_memory(),})


class AlreadyAnswered(View):
    template_name = 'trivia/already_answered.html'

    def get(self, request):
        return render(request, self.template_name, {'display_memory': utils.get_memory(),})