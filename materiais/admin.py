from django.contrib import admin

from .models import Categoria, Arquivo

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Arquivo)
