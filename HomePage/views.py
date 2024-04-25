from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

def PageView(request):
        if request.user.is_authenticated:
            return render(request, 'homepage/homepage.html')
        else:
            return HttpResponse('Usuario não conectado')
# class HomePageView(request):
        # Renderiza a pagina de homepage
        # template_name = 'homepage/homepage.html'
        # return template_name