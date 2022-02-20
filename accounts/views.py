from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .forms import SignUpForm

def UserRegisterView(request):
    data = {}
    data["SignUpForm"] = SignUpForm
    return render(request, "registration/signup.html", data) 