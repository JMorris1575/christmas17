from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View

from .models import TriviaQuestion, TriviaChoices, TriviaUserResponse

import utils


# Create your views here.


class Scoreboard(View):
    template_name = 'trivia/scoreboard.html'

    def get(self, request):
        return render(request, self.template_name, {'display_memory': utils.get_memory(),})

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
        choice_index = request.POST['choice']
        question = TriviaQuestion.objects.get(number=question_number)
        choice = TriviaChoices.objects.filter(question=question).get(number=choice_index)
        correct_choice = TriviaChoices.objects.filter(question=question).get(correct=True)
        print('correct_choice.index = ', correct_choice.index())
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

