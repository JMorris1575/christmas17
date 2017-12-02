from django.shortcuts import render
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
        user_response = TriviaUserResponse(user=request.user, question=question, response=choice)
        user_response.save()

        return render(request, self.template_name, {'display_memory': utils.get_memory(),
                                                    'question': question,
                                                    'choice': choice})
