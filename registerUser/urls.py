from django.urls import path
from .views import renderForm as Register_Views

urlpatterns = [
    path('register/', Register_Views, name='views'),
]
