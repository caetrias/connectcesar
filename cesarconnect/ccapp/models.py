from django.db import models

# Create your models here

# class Login(models.Model):
#     #email = 
#     nome = models.CharField(max_length=200)
#     #senha = 

class Perfil(models.Model):   #NAO UTILIZAR ESSE MODEL - FOI USADO COMO TESTE - DESCOBRIR COMO DESINSTALAR
    nome = models.CharField(max_length=200)
    descricao = models.TextField(null=True, blank=True)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nome

class Usuario(models.Model): 
    id_usuario = models.AutoField(primary_key=True) 
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    senha = models.CharField(max_length=200)
    descricao = models.TextField(null=True, blank=True)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    senha = models.TextField(max_length=255)
    descricao = models.TextField(null=True, blank=True)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)