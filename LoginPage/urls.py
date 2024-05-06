from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'main'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.lista_produtos, name='lista_produtos'),
    path('login/', include('login.urls')),
    path('HomePage/', include('HomePage.urls')),
    path('', include('registerUser.urls')),
    path('produto/<int:produto_id>/', views.visualizar_produto, name='visualizar_produto'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)