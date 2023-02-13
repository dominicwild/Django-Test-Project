from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class UserLoginView(LoginView):
    template_name = "recipe_site/login.html"
    next = "recipe_site/home.html"
