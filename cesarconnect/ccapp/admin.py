from django.contrib import admin

# Register your models here.

from .models import Grupo
from .models import Pessoa

admin.site.register(Grupo)
admin.site.register(Pessoa)