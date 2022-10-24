from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("estas en el home")

def signup(request):
    return HttpResponse("estas en el signup")

def signin(request):
    return HttpResponse("estas en el signin")

def sigout(request):
    return HttpResponse("etas en el signout")