from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden, HttpResponseRedirect
from .forms import ProdutoForm, ImageUploadForm
from django.http import JsonResponse
from .models import Produtos, PerfilUsuario, Tag
import json
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

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
                return redirect('HomePage')
        else:
            return HttpResponse("O perfil do usuário não está definido.")
    else:
        if request.user.is_authenticated:
            nome = request.user
            email = request.user.email
        else:
            return HttpResponse('Usuário não conectado')
        form = ImageUploadForm(instance=request.user.perfilusuario)
    return render(request, 'homepage/index.html', {'nome': nome, 'email': email, 'form': form})

def SellView(request):
        if request.user.is_authenticated:
            produtos = Produtos.objects.filter(user=request.user)
            return render(request, 'homepage/pagina3.html', {'produtos': produtos})
        else:
            return HttpResponse('Usuario não conectado')

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
                return redirect('/HomePage/ProdutosSell')  # Adicionado '/' antes de 'HomePage'
            except Exception as e:
                error_message = "Erro ao criar o produto: {}".format(e)
                return render(request, 'homepage/ProdutosSell', {'form': form, 'error_message': error_message})
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