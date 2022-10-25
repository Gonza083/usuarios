from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def home(request):
    return render(request, "home.html", {})

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('task')
            except:
                return render(request, 'signup.html', {
                    'error': 'Username already exists ',
                    'form': UserCreationForm,
                    })
        return render(request, 'signup.html', {
            'error': 'password do not match',
            'form': UserCreationForm,
            })

def signin(request):
    return HttpResponse("estas en el signin")

def singout(request):
    logout(request)
    return redirect('home')

