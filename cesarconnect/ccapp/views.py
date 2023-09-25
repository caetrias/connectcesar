from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def tela_inicial(request):
    return render(request, 'tela_inicial.html')

def criargrupo(request):
    return render(request, 'criargrupo.html')

def meugrupo(request):
    return render(request, 'meugrupo.html')