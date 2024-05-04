from django.shortcuts import render
from HomePage.models import Produtos

def search(request):
    query = request.GET.get('q')
    if query:
        results = Produtos.objects.filter(nome__icontains=query)
    else:
        results = []
    return render(request, 'mainpage/index.html', {'results': results})
