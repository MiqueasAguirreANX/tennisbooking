from django.contrib import admin
from django.urls import path
from pages.views import (
    CourtDetailsView,
    DeleteBookedView,
    HomeView,
    CreateCourtView,
    AllBookedView,
    LoginView,
    LogoutView,
    SignUpView
)

app_name = "pages"

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('create-court/', CreateCourtView.as_view(), name="create-court"),
    path('all-booked/', AllBookedView.as_view(), name="all-booked"),
    path('court-details/<int:court_id>/', CourtDetailsView.as_view(), name="court-details"),
    path('delete-booked/<int:booked_id>/', DeleteBookedView.as_view(), name="delete-booked"),


    path('tennis-login/', LoginView.as_view(), name="tennis-login"),
    path('tennis-signup/', SignUpView.as_view(), name='tennis-signup'),
    path('tennis-logout/', LogoutView.as_view(), name='tennis-logout'),
]