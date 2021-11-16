from datetime import datetime
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from courts.models import Court, DateBooked
# Create your views here.


class GetAllCourtsView(APIView):
    permissions = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        data = []
        courts = Court.objects.all()
        
        for court in list(courts):
            dates = [str(x.date) for x in list(DateBooked.objects.filter(court=court)) if x.date >= datetime.today().date()]
            data.append(dict(
                pk=court.pk,
                manager_user=court.manager_user.pk,
                latitude=court.latitude,
                longitude=court.longitude,
                dates=dates,
                name=court.name,
            ))
            
        return Response(data=data, status=200)


class BookCourtView(APIView):
    permissions = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        date_to_book = data.get('date')
        court_id = int(data.get('court_id'))

        court = Court.objects.filter(pk=court_id)

        if court.exists():
            dates_booked = DateBooked.objects.filter(court=court.first())
            if dates_booked.exists():
                for date in dates_booked:
                    if str(date.date) == str(date_to_book):
                        return Response(data=dict(
                            status="book-already-exists",
                            message=f'Date ocupied'
                        ), status=200)

            date_to_add = DateBooked(date=date_to_book, court=court.first(), user=request.user)
            date_to_add.save()

            return Response(data=dict(
                status="book-added",
                message=f'You booked the court at time {date_to_add.date}'
            ), status=200)
        else:
            return Response(data=dict(
                status="error",
                message="Court doesnt found"
            ), status=404)


class CreateCourtView(APIView):
    permissions = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            print(data)
            court = Court(
                manager_user=request.user, 
                latitude=data.get('current_lat'),
                longitude=data.get('current_lng'),
                name=data.get('name'),
            )
            court.save()
            return Response(data=dict(
                status="court-created",
                message='The Court was created'
            ), status=200)
        except Exception as e:
            print(e)
            return Response(data=dict(
                status="error",
                message='Some error has ocurred'
            ), status=400)
