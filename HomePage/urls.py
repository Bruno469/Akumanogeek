from django.urls import path
from . import views

app_name = 'HomePage'

urlpatterns = [
    path('', views.PageView, name='homepage'),
    path('AddProduto', views.Add_Produto, name='add_produto'),
    path('AddProduto/<int:objeto_id>', views.Add_Produto, name='add_produto'),
]