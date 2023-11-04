from django.shortcuts import render, redirect
from .models import Pessoa, Grupo
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        try:
            pessoa = Pessoa.objects.get(email=email, senha=senha)
            request.session['pessoa_id'] = pessoa.id_usuario
            return redirect('tela_inicial')
        except Pessoa.DoesNotExist:
            return render(request, "senhaincorreta.html")


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if Pessoa.objects.filter(email=email).exists():
            return render(request, "emailinvalido.html")
        
        novo_usuario = Pessoa()
        novo_usuario.nome = username
        novo_usuario.email = email
        novo_usuario.senha = senha
        novo_usuario.save()

        try:
            pessoa = Pessoa.objects.get(email=email, senha=senha)
            request.session['pessoa_id'] = pessoa.id_usuario
            return redirect('tela_inicial')
        except Pessoa.DoesNotExist:
            return render(request, "senhaincorreta.html")
    
        

def tela_inicial(request):
    if 'pessoa_id' in request.session:
        pessoa_id = request.session['pessoa_id']
        pessoa = Pessoa.objects.get(id_usuario=pessoa_id)
        nome_usuario = pessoa.nome
        grupos = Grupo.objects.all()
        context = {
            'nome_usuario': nome_usuario,
            'grupos' : grupos
        }
        return render(request, 'tela_inicial.html', context)
    else:
        return redirect('login')


def criargrupo(request):
    if request.method == "GET":
        return render(request, 'criargrupo.html')
    else:
        nome_grupo = request.POST.get('nome_grupo')
        descricao_grupo = request.POST.get('descricao_grupo')
        periodo = request.POST.get('periodo')
        
        if Grupo.objects.filter(nome_grupo = nome_grupo).exists():
            return render(request, "grupo_invalido.html")
        
        novo_grupo = Grupo()
        novo_grupo.nome_grupo = nome_grupo
        novo_grupo.descricao_grupo = descricao_grupo
        novo_grupo.periodo = periodo
        novo_grupo.save()

        pessoa = Pessoa.objects.get(id_usuario=request.session['pessoa_id'])

        pessoa.grupo_criado = novo_grupo
        pessoa.save()
        
        try:
            request.session['grupo_id'] = novo_grupo.id_grupo
            return redirect('meugrupo')
        except Grupo.DoesNotExist:
            return HttpResponse("Grupo não existe")


def meugrupo(request):
    grupo_id = request.session.get('grupo_id', None)

    if grupo_id is None:
        return render(request, 'grupo_nao_pertence.html')
    
    try:
        grupo = Grupo.objects.get(id_grupo=grupo_id)
    except Grupo.DoesNotExist:
        return render(request, 'grupo_inexistente.html')
    
    if 'pessoa_id' in request.session:
        pessoa_id = request.session['pessoa_id']
        pessoa = Pessoa.objects.get(id_usuario=pessoa_id)
        nome_usuario = pessoa.nome

        if pessoa.grupo_criado == grupo:
            context = {
                'nome_usuario': nome_usuario,
                'grupo': grupo,
            }
            return render(request, 'meugrupo.html', context)
        
        return render(request, 'grupo_sem_acesso.html')
    

def acessarperfil(request):
    if 'pessoa_id' in request.session:
        pessoa_id = request.session['pessoa_id']
        pessoa = Pessoa.objects.get(id_usuario=pessoa_id)
        context = {
            'nome': pessoa.nome,
            'periodo': pessoa.periodo,
            'descricao': pessoa.descricao,
            'mbti': pessoa.mbti,
            'curso': pessoa.curso,
            'foto': pessoa.foto,
            'idade': pessoa.idade
        }
        return render(request, 'acessarperfil.html', context)

def editar_perfil(request):
    if request.method == 'GET':
        return render(request, 'editar_perfil.html')
    else:
        user = Pessoa.objects.get(id_usuario=request.session['pessoa_id'])
        user.nome = request.POST['nome']
        user.idade = request.POST['idade']
        user.mbti = request.POST['mbti']
        user.periodo = request.POST['periodo']
        user.curso = request.POST['curso']
        user.foto = request.FILES.get('foto')
        user.descricao = request.POST['descricao']
        user.save()
        return render(request, 'tela_inicial.html')

def emailinvalido(request):
    return render(request, 'emailinvalido.html')

def senhaincorreta(request):
    return render(request, 'senhaincorreta.html')

def grupo_invalido(request):
    return render(request, 'grupo_invalido.html')

def grupo_nao_pertence(request):
    return render(request, 'grupo_nao_pertence.html')

def grupo_sem_acesso(request):
    return render(request, 'grupo_sem_acesso.html')

def grupo_inexistente(request):
    return render(request, 'grupo_inexistente.html')

def resultado_pesquisa(request):
    if request.method == "GET":
        busca = request.GET.get("pesquisa")

        resultados_pessoa = Pessoa.objects.filter(nome__icontains=busca)
        resultados_grupo = Grupo.objects.filter(nome_grupo__icontains=busca)

        context = {
            'resultados_pessoa': resultados_pessoa,
            'resultados_grupo': resultados_grupo,
            'busca': busca,
        }

        return render(request, 'resultado_pesquisa.html', context)
    
def acesso_pessoa(request, id_field):
    id_pessoa = Pessoa.objects.get(id_usuario = id_field)
    context = {'pessoa': id_pessoa}
    return render(request, 'acesso_pesquisa.html', context)

def acesso_grupo(request, id_field):
    grupo_id = Grupo.objects.get(id_grupo = id_field)
    criador_grupo = Pessoa.objects.filter(grupo_criado_id = grupo_id)
    context = {
        'grupo': grupo_id,
        'criador' : criador_grupo
    }
    return render(request, 'acesso_pesquisa.html', context)

def editar_grupo(request, grupo_id):
    if 'pessoa_id' in request.session:
        pessoa_id = request.session['pessoa_id']
        grupo_id = int(grupo_id)

        try:
            pessoa = Pessoa.objects.get(id_usuario=pessoa_id)

            if pessoa.grupo_criado and pessoa.grupo_criado.id_grupo == grupo_id:
                grupo = Grupo.objects.get(id_grupo=grupo_id)

                if request.method == 'POST':
                    grupo.nome_grupo = request.POST.get('nome_grupo')
                    grupo.descricao_grupo = request.POST.get('descricao_grupo')
                    grupo.periodo_grupo = request.POST.get('periodo_grupo')
                    grupo.foto_grupo = request.FILES.get('foto_grupo')
                    grupo.save()
                    return redirect('meugrupo')
                
                context = {'grupo': grupo}
                return render(request, 'editar_grupo.html', context)
            
            else:
                return HttpResponseForbidden("Você não tem permissão para editar este grupo.")
        except (Pessoa.DoesNotExist, Grupo.DoesNotExist):
            return render(request, 'grupo_inexistente.html')
        
    else:
        return redirect('login')