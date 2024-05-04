from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden, HttpResponseRedirect
from .forms import ProdutoForm
from django.http import JsonResponse
from .models import Produtos, UserImg

def PageView(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            formulario = UserImg(request.POST, request.FILES)
            if formulario.is_valid():
                user_id = request.user.id
                imgUSER = formulario.cleaned_data['imagem']
                try:
                    produto = Produtos.objects.create(user_id=user_id, imgUSER=imgUSER)
                    print("Imagem alterada com sucesso.")
                    return HttpResponseRedirect(request.path_info)
                except Exception as e:
                    print("Erro ao salvar imagem:", e)
                    return render(request, 'homepage/index.html', {'nome': nome, 'email': email, 'userimg': imgUSER, 'error_message': str(e)})
            else:
                # Se o formulário for inválido, retorne o formulário com erros para o template
                return render(request, 'homepage/index.html', {'nome': nome, 'email': email, 'userimg': imgUSER, 'formulario': formulario})
        else:
            formulario = UserImg()  # Crie uma instância vazia do formulário
            
        try:
            nome = request.user
            imgUSER = UserImg.objects.get(user=nome)
        except UserImg.DoesNotExist:
            imgUSER = 'media/default.avif'

        nome = request.user
        email = request.user.email

        return render(request, 'homepage/index.html', {'nome': nome, 'email': email, 'imgUSER': imgUSER, 'formulario': formulario})
    else:
        return HttpResponse('Usuario não conectado')

def SellView(request):
        if request.user.is_authenticated:
            produtos = Produtos.objects.filter(user=request.user)
            return render(request, 'homepage/pagina3.html', {'produtos': produtos})
        else:
            return HttpResponse('Usuario não conectado')

def Add_Produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        print("Formulário recebido:", form)  # Adicionando print para verificar o formulário recebido
        if form.is_valid():
            nome = form.cleaned_data['nome']
            imagem = form.cleaned_data['imagem']
            description = form.cleaned_data['description']
            quantidade = form.cleaned_data['quantidade']
            valor = form.cleaned_data['valor']
            tags = request.POST.getlist('tags[]')
            print("Dados do formulário válidos.")  # Adicionando print para verificar se os dados do formulário são válidos

            # Obtenha o ID do usuário atual
            user_id = request.user.id
            print("ID do usuário atual:", user_id)  # Adicionando print para verificar o ID do usuário atual

            try:
                # Salve o produto no banco de dados com o ID do usuário
                produto = Produtos.objects.create(user_id=user_id, nome=nome, description=description, imagem=imagem, valor=valor, quantidade=quantidade)
                produto.tags.add(*[tag.strip() for tag in tags.split(',')])
                print("Produto criado com sucesso.")  # Adicionando print para verificar se o produto foi criado com sucesso

                return redirect('HomePage/ProdutosSell')
            except Exception as e:
                print("Erro ao criar o produto:", e)
                return render(request, 'homepage/ProdutosSell', {'form': form, 'error_message': str(e)})
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