from django.http import HttpResponse
from django.shortcuts import render

from . import session

def index(request):
    print(request)
    return render(request, 'index.html')

def go(request, session):
    return HttpResponse("Welcome to your session {}. <br> It is nice and fun but chill out for now".format(session))

def createsession(request):
    session_id = session.cratesession()
    return HttpResponse("Your session is {}".format(session_id))
