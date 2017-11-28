from django.shortcuts import render
from django.views.generic import View


# Create your views here.


class Scoreboard(View):
    template_name = 'trivia/scoreboard.html'

    def get(self, request):
        return render(request, self.template_name)

class DisplayQuestion(View):
    print('Got to DisplayQuestion view')


class DisplayResult(View):
    print('Got to DisplayResult view')
