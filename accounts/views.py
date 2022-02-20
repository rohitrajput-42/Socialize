from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.models import User, auth
import re

def UserRegisterView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        value = {}
        value['username'] = username
        value['email'] = email

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.error(request, "Username already registered, Please try some other username !!!!....")
                return render(request, "registration/signup.html", {"value": value})    
            elif User.objects.filter(email = email).exists():
                messages.error(request, "Email already in use, Please continue with some other email !!!!....")
                return render(request, "registration/signup.html", {"value": value}) 
            else:
                user = User(username = username, email = email, password = password1)
                user.save()
                return render(request, 'registration/login.html')

        else:
            messages.error(request, "Password not matching, Please try again !!!!....")
            return render(request, "registration/signup.html", {"value": value}) 

    else:
        return render(request, "registration/signup.html") 

def Login(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials, Please try again !!!!...")
            return render(request, "registration/login.html")

    else:
        return render(request, "registration/login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')