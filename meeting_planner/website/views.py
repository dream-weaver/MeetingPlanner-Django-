from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from meetings.models import Meeting

def welcome(request):
    title = 'Welcome to the meeting planner'
    num_meetings = Meeting.objects.count()
    meetings = Meeting.objects.all()
    return render(request, "website/welcome.html", {'title': title, 'num_meetings': num_meetings, 'meetings': meetings})

def date(request):
    return HttpResponse("This webpage is served at " + str(datetime.now()))

def about(request):
    return HttpResponse("This is an about page!")
