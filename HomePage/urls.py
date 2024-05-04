from django.urls import include, path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'HomePage'

urlpatterns = [
    path('', views.PageView, name='homepage'),
    path('AddProduto', views.Add_Produto, name='add_produto'),
    path('AddProduto/<int:objeto_id>', views.Add_Produto, name='add_produto'),
    path('ProdutosSell', views.SellView, name='SellView'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)