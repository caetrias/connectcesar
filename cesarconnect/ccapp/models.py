from django.db import models

# Create your models here
class Grupo(models.Model):
    id_grupo = models.AutoField(primary_key=True)
    nome_grupo = models.CharField(max_length=255)
    descricao_grupo = models.TextField()
    periodo = models.CharField(max_length=255)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

class Pessoa(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    senha = models.TextField(max_length=255)
    descricao = models.TextField(null=True, blank=True)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)
    grupo_criado = models.ForeignKey(Grupo, null=True, blank=True, on_delete=models.SET_NULL)
