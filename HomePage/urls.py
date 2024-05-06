from django.urls import include, path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'HomePage'

urlpatterns = [
    path('', views.upload_image, name='homepage'),
    path('AddProduto', views.Add_Produto, name='add_produto'),
    path('EditProduto/<int:objeto_id>', views.editar_produto, name='add_produto'),
    path('ProdutosSell', views.SellView, name='SellView'),
    path('logout/', views.logout_view, name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)