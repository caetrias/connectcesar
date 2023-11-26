#URLS DO APP

from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('cadastro/', views.cadastro, name="cadastro"),
    path('tela_inicial/', views.tela_inicial, name="tela_inicial"),
    path('criargrupo/', views.criargrupo, name="criargrupo"),
    path('meugrupo/', views.meugrupo, name="meugrupo"),
    path('acessarperfil/', views.acessarperfil, name="acessarperfil"),
    path('editar_perfil/', views.editar_perfil, name="editar_perfil"),
    path('emailinvalido/', views.emailinvalido, name="emailinvalido"),
    path('senhaincorreta/', views.senhaincorreta, name="senhaincorreta"),
    path('grupo_invalido/', views.grupo_invalido, name="grupo_invalido"),
    path('resultado_pesquisa/', views.resultado_pesquisa, name='resultado_pesquisa'),
    path('acesso/pessoa/<int:id_field>/', views.acesso_pessoa, name='acesso_pessoa'),
    path('acesso/grupo/<int:id_field>/', views.acesso_grupo, name='acesso_grupo'),
    path('grupo_nao_pertence/', views.grupo_nao_pertence, name='grupo_nao_pertence'),
    path('grupo_sem_acesso/', views.grupo_sem_acesso, name='grupo_sem_acesso'),
    path('grupo_inexistente/', views.grupo_inexistente, name='grupo_inexistente'),
    path('editar_grupo/<int:grupo_id>', views.editar_grupo, name="editar_grupo"),
    path('deletar_grupo/<int:pk>/', views.deletar_grupo, name="deletar_grupo"),
]