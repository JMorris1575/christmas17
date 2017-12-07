from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class UnderConstruction(View):
    template_name = 'under_construction/under-construction.html'

    def get(self, request):
        return render(request, self.template_name)