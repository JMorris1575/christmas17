from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class LoginError(View):
    template_name = 'user/login_error.html'

    def get(self, request):
        return render(request, self.template_name, {})

