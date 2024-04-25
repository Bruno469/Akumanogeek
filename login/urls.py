from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('verification/', LoginView.as_view(), name='verification'),
]
