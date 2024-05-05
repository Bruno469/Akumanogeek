from django.shortcuts import render, get_object_or_404
from HomePage.models import Produtos, Tag

def lista_produtos(request):
    produtos = Produtos.objects.all()
    return render(request, 'mainpage/index.html', {'produtos': produtos})

def visualizar_produto(request, produto_id):
    produto = get_object_or_404(Produtos, pk=produto_id)
    return render(request, 'mainpage/visualizer.html', {'produto': produto})