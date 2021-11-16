from django.contrib import admin
from django.urls import path
from courts.views import (
   CreateCourtView,
   GetAllCourtsView, 
   BookCourtView
) 

app_name = "courts"

urlpatterns = [
    path('get-all-courts/', GetAllCourtsView.as_view(), name="get-all-courts"),
    path('book-court/', BookCourtView.as_view(), name="book-court"),
    path('create-court/', CreateCourtView.as_view(), name="create-court"),
]