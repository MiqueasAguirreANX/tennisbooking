from datetime import datetime
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from courts.models import Court, DateBooked
from tennisbooking.settings import AUTH_PASSWORD_VALIDATORS

# Create your views here.

class HomeView(LoginRequiredMixin, View):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        context = dict(google_api_key=settings.GOOGLE_API_KEY)
        return render(request, self.template_name, context)


class CreateCourtView(LoginRequiredMixin, View):
    template_name = "create-court.html"

    def get(self, request, *args, **kwargs):
        context = dict(google_api_key=settings.GOOGLE_API_KEY)
        return render(request, self.template_name, context)


class AllBookedView(LoginRequiredMixin, View):
    template_name = "books.html"

    def get(self, request, *args, **kwargs):
        dates_booked = DateBooked.objects.filter(user=request.user)
        context = dict(dates_booked=[x for x in list(dates_booked) if x.date >= datetime.today().date()])
        return render(request, self.template_name, context)


class DeleteBookedView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        date_booked = DateBooked.objects.filter(user=request.user, pk=kwargs.get("booked_id"))
        if date_booked.exists():
            date_booked.first().delete()

        return redirect("/all-booked/")

class CourtDetailsView(LoginRequiredMixin, View):
    template_name = "court-details.html"

    def get(self, request, *args, **kwargs):
        court = Court.objects.filter(pk=kwargs["court_id"])
        context = dict(google_api_key=settings.GOOGLE_API_KEY)
        if court.exists():
            court = court.first()
            context.update(dict(
                latitude=court.latitude,
                longitude=court.longitude,
                court_name=court.name,
            ))
        else:
            return redirect('/all-booked/')
            
        return render(request, self.template_name, context)


class LoginView(View):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        context = dict()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        user = authenticate(request, username=request.POST.get("username"), password=request.POST.get("password"))
        if user:
            login(request, user)

        return redirect('/')


class SignUpView(View):
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        context = dict()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        data = request.POST
        print(data)
        if data.get("username") != "" and len(data.get("username")) > 7:
            if data.get("password1") != "" and len(data.get("password1")) > 7 and data.get("password1") == data.get("password2"):
                User.objects.create_user(username=data.get("username"), password=data.get("password1"))
                user = authenticate(request, username=data.get("username"), password=data.get("password1"))
                print(user)
                if user:
                    login(request, user)
                    return redirect('/')
                else:
                    return redirect('/tennis-login/')

        return redirect('/tennis-signup/')

class LogoutView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')