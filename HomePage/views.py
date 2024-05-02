from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from .forms import ProdutoForm

def PageView(request):
        if request.user.is_authenticated:
            return render(request, 'homepage/homepage.html')
        else:
            return HttpResponse('Usuario não conectado')

def Add_Produto(request, objeto_id):
    objeto = get_object_or_404(MeuObjeto, pk=objeto_id)
    if objeto.user != request.user:
        return HttpResponseForbidden("Você não tem permissão.")
    if request.method == 'POST':
        nome = request.POST.get('nome')
        imagem = request.FILES.get('imagem')
        valor = request.POST.get('valor')
        tags = request.POST.get('tags')

        # Processar as tags
        tags_lista = [tag.strip() for tag in tags.split(',')]

        # Salvar o produto no banco de dados, associando as tags
        produto = Produto.objects.create(nome=nome, imagem=imagem, valor=valor)
        produto.tags.add(*tags_lista)

        # Redirecionar para uma página de sucesso ou fazer qualquer outra coisa necessária
        return redirect('homepage/homepage.html')

    # Se for uma requisição GET, renderize o formulário
    form = ProdutoForm()
    return render(request, 'homepage/adicionar_produto.html', {'form': form})
# class HomePageView(request):
        # Renderiza a pagina de homepage
        # template_name = 'homepage/homepage.html'
        # return template_name