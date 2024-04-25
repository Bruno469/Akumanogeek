from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

def renderForm(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            passworld = form.cleaned_data['password']

            NewUser = User.objects.create_user(username=nome, email=email, password=passworld)
            NewUser.save()
            return redirect('../login')
        else:
            print("[!] Erros de validação encontrados:", form.errors)
    else:
        form = SignUpForm()
    return render(request, 'register/register.html', {'form': form})
