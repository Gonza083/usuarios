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
                return redirect('home')
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
    if request.method == 'GET':
        return render(request, 'signin.html', {'form': AuthenticationForm})
    else:
        user= authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
    if user is None:
        return render(request,'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})
    
    login(request, user)
    return redirect('home')

def singout(request):
    logout(request)
    return redirect('home')

