from django.contrib.auth.backends import ModelBackend
from .models import Pessoa

class CustomBackend(ModelBackend):
    def authenticate(self, request, email=None, senha=None, **kwargs):
        try:
            user = Pessoa.objects.get(email=email, senha=senha)
            return user
        except Pessoa.DoesNotExist:
            return None