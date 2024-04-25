from django.urls import path
from .views import registra

urlpatterns = [
    path('', registra, name='register'),
]