#URLS DO APP

from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('cadastro/', views.cadastro, name="cadastro"),
    path('tela_inicial/', views.tela_inicial, name="tela_inicial"),
    path('criargrupo/', views.criargrupo, name="criargrupo"),
    path('meugrupo/', views.meugrupo, name="meugrupo"),
    
]