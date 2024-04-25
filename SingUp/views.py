from django.shortcuts import render, redirect
from .forms import SingUpForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User

def registra(request):
    if request.method == 'POST':
        form = SingUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            email=form.cleaned_data['email'],
                                            password=form.cleaned_data['password1'])
            user.save()
            return redirect('../login')
    else:
        form = SingUpForm()
    return render(request, 'register/register.html', {'form': form})