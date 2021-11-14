from django.shortcuts import render
from django.views.generic import View
from django.conf import settings

# Create your views here.

class HomeView(View):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        context = dict(google_api_key=settings.GOOGLE_API_KEY)
        return render(request, self.template_name, context)
