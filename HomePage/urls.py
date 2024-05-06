from django.urls import include, path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'HomePage'

urlpatterns = [
    path('', views.upload_image, name='homepage'),
    path('AddProduto', views.Add_Produto, name='add_produto'),
    path('EditProduto/<int:produto_id>/', views.editar_produto, name='editar_produto'),
    path('ProdutosSell', views.SellView, name='SellView'),
    path('Comprar', views.Finalizar_Compra, name='Finalizar_Compra'),
    path('AddCarrinho/<int:produto_id>/', views.adicionar_carrinho, name='adicionar_carrinho'),
    path('Carrinho/', views.mostrar_produtos_carrinho, name='mostrar_produtos_carrinho'),
    path('logout/', views.logout_view, name='logout'),
    path('DeleteProduto/<int:produto_id>/', views.deletar_produto, name='deletar_produto')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)