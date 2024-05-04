from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from .forms import ProdutoForm
from django.http import JsonResponse
from .models import Produtos

def PageView(request):
        if request.user.is_authenticated:
            produtos = Produtos.objects.all()
            return render(request, 'homepage/homepage.html', {'produtos': produtos})
        else:
            return HttpResponse('Usuario não conectado')


def Add_Produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            imagem = form.cleaned_data['imagem']
            valor = form.cleaned_data['valor']
            tags = request.POST.getlist('tags[]')

            # Obtenha o ID do usuário atual
            user_id = request.user.id

            try:
                # Salve o produto no banco de dados com o ID do usuário
                produto = Produtos.objects.create(user_id=user_id, nome=nome, imagem=imagem, valor=valor)
                produto.tags.add(*[tag.strip() for tag in tags.split(',')])

                return redirect('HomePage')
            except Exception as e:
                return render(request, 'homepage/adicionar_produto.html', {'form': form, 'error_message': str(e)})
    else:
        form = ProdutoForm()
    return render(request, 'homepage/adicionar_produto.html', {'form': form})



def Edit_Produto(request, objeto_id=None):
    if objeto_id:
        # Se um objeto_id for fornecido, verifique se ele existe
        objeto = get_object_or_404(MeuObjeto, pk=objeto_id)
        if objeto.user != request.user:
            return HttpResponseForbidden("Você não tem permissão.")
    else:
        # Se nenhum objeto_id for fornecido, não há necessidade de verificar a permissão
        objeto = None

# class HomePageView(request):
        # Renderiza a pagina de homepage
        # template_name = 'homepage/homepage.html'
        # return template_name