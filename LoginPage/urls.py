from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.search, name='search'),
    path('login/', include('login.urls')),
    path('HomePage/', include('HomePage.urls')),
    path('', include('registerUser.urls')),
]
