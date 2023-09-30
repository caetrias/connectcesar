from django.contrib import admin

# Register your models here.

from .models import Perfil
from .models import Usuario

admin.site.register(Perfil)
admin.site.register(Usuario)