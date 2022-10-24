from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "home.html", {})

def signup(request):
    return HttpResponse("estas en el signup")

def signin(request):
    return HttpResponse("estas en el signin")

def logout(request):
    return HttpResponse("etas en el logout")