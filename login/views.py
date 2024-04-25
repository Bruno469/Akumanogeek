from django.shortcuts import render
from django.contrib.auth.views import LoginView as BaseLoginView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views import View
from django.shortcuts import redirect

class LoginView(BaseLoginView):
    # Renderiza a pagina de login
    template_name = 'login/login.html'