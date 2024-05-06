from django.shortcuts import render, get_object_or_404
from HomePage.models import Produtos, Tag

def lista_produtos(request):
    if 'q' in request.GET:
        query = request.GET['q']
        resultados = Produtos.objects.filter(nome__icontains=query)
    else:
        resultados = []
    produtos = Produtos.objects.all()
    return render(request, 'mainpage/index.html', {'produtos': produtos, 'resultados': resultados})

def visualizar_produto(request, produto_id):
    produto = get_object_or_404(Produtos, pk=produto_id)
    return render(request, 'mainpage/visualizer.html', {'produto': produto})