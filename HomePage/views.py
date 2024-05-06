from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden, HttpResponseRedirect
from .forms import ProdutoForm, ImageUploadForm
from django.http import JsonResponse
from .models import Produtos, PerfilUsuario, Tag, carrinho
import json
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import logout

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        PerfilUsuario.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.perfilusuario.save()

def upload_image(request):
    if request.method == 'POST':
        if hasattr(request.user, 'perfilusuario'):
            form = ImageUploadForm(request.POST, request.FILES, instance=request.user.perfilusuario)
            if form.is_valid():
                form.save()
                return redirect('/HomePage')
        else:
            return HttpResponse("O perfil do usuário não está definido.")
    else:
        if request.user.is_authenticated:
            nome = request.user
            email = request.user.email
        else:
            return redirect('/login')
        form = ImageUploadForm(instance=request.user.perfilusuario)
    return render(request, 'homepage/index.html', {'nome': nome, 'email': email, 'form': form})

def SellView(request):
        if request.user.is_authenticated:
            produtos = Produtos.objects.filter(user=request.user)
            return render(request, 'homepage/pagina3.html', {'produtos': produtos})
        else:
            return redirect('/login')

def Add_Produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            imagem = form.cleaned_data['imagem']
            description = form.cleaned_data['description']
            quantidade = form.cleaned_data['quantidade']
            valor = form.cleaned_data['valor']

            user_id = request.user.id

            try:
                produto = Produtos.objects.create(user_id=user_id, nome=nome, description=description, imagem=imagem, valor=valor, quantidade=quantidade)
                tags = json.loads(request.POST.get('tags'))
                for tag_text in tags:
                    tag, created = Tag.objects.get_or_create(nome=tag_text)
                    produto.tags.add(tag)
                return redirect('/HomePage/ProdutosSell')
            except Exception as e:
                error_message = "Erro ao criar o produto: {}".format(e)
                return render(request, 'homepage/ProdutosSell', {'form': form, 'error_message': error_message})
    else:
        form = ProdutoForm()
    return render(request, 'homepage/adicionar_produto.html', {'form': form})



def editar_produto(request, produto_id):
    produto = get_object_or_404(Produtos, pk=produto_id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('LoginPage:produto', produto_id=produto_id)
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'homepage/editar_produto.html', {'form': form, 'produto': produto, 'produto_id': produto_id})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('/login'))

def deletar_produto(request, produto_id):
    carrinho_usuario = carrinho.objects.filter(user=request.user).first()
    if carrinho_usuario:
        produto = Produtos.objects.get(pk=produto_id)
        carrinho_usuario.carrinho_compras.remove(produto)
    
    return redirect('HomePage:mostrar_produtos_carrinho')

def adicionar_carrinho(request, produto_id):
    produto = get_object_or_404(Produtos, pk=produto_id)
    carrinho_usuario, created = carrinho.objects.get_or_create(user=request.user)
    carrinho_usuario.carrinho_compras.add(produto)
    return redirect('/')


def mostrar_produtos_carrinho(request, produto_id=None):
    carrinho_usuario = carrinho.objects.filter(user=request.user).first()
    if request.method == 'POST':
        if produto_id is not None:
            produto = get_object_or_404(Produtos, pk=produto_id)
            carrinho_usuario.carrinho_compras.remove(produto)

    if carrinho_usuario:
        produtos_no_carrinho = carrinho_usuario.carrinho_compras.all()
    else:
        produtos_no_carrinho = []

    return render(request, 'mainpage/carrinho.html', {'produtos_no_carrinho': produtos_no_carrinho})

def Finalizar_Compra(request):
    carrinho_usuario = carrinho.objects.filter(user=request.user).first()
    
    if carrinho_usuario:
        produtos_no_carrinho = carrinho_usuario.carrinho_compras.all()
    else:
        produtos_no_carrinho = []

    return render(request, 'mainpage/comprando.html', {'produtos_no_carrinho': produtos_no_carrinho})


# class HomePageView(request):
        # Renderiza a pagina de homepage
        # template_name = 'homepage/homepage.html'
        # return template_name