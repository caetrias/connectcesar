from django.db import models

# Create your models here

# class Login(models.Model):
#     #email = 
#     nome = models.CharField(max_length=200)
#     #senha = 

class Perfil(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(null=True, blank=True)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nome

