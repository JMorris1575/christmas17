from django.shortcuts import render
from django.views.generic import View

import utils


# Create your views here.


class Scoreboard(View):
    template_name = 'trivia/scoreboard.html'

    def get(self, request):
        return render(request, self.template_name, {'display_memory': utils.get_memory(),})

class DisplayQuestion(View):
    template_name = 'trivia/trivia_question.html'

    def get(self, request, question_number=None):
        return render(request, self.template_name, {'display_memory': utils.get_memory(),
                                                    'q_number': question_number})


class DisplayResult(View):
    template_name = 'trivia/trivia_result.html'

    def get(self, request, question_number=None):
        return render(request, self.template_name, {'display_memory': utils.get_memory(),
                                                    'q_number': question_number})
