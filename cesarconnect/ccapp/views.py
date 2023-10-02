from django.shortcuts import render
from .models import Pessoa
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_django

# Create your views here.

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)

            return render(request, 'tela_inicial.html')
        else:
            return HttpResponse("Email ou senha inválidos!")

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(email=email).first()

        if user:
            return HttpResponse('Email já cadastrado!')
        
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        
        return render(request, 'tela_inicial.html')
        

def tela_inicial(request):
    return render(request, 'tela_inicial.html')

def criargrupo(request):
    return render(request, 'criargrupo.html')

def meugrupo(request):
    return render(request, 'meugrupo.html')

def acessarperfil(request):
    return render(request, 'acessarperfil.html')

def editar_perfil(request):
    return render(request, 'editar_perfil.html')



def listagemusuarios(request):
    # salvar os dados na tela para o banco de dados
    novo_usuario= Pessoa()
    novo_usuario.email= request.POST.get('email')
    novo_usuario.senha= request.POST.get('senha')
    novo_usuario.save()

    # exibir todos os usuarios ja cadastrados em uma nova pagina
    usuarios = {
        'usuarios': Pessoa.objects.all()
    }

    # retornar os dados dos usuarios para a página
    return render(request, 'listagemusuarios.html', usuarios)
