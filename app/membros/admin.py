from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Membro, Filho

@admin.register(Membro)
class MembroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo', 'email', 'telefone', 'tipo_membro')
    search_fields = ('nome', 'email', 'codigo')
    list_filter = ('tipo_membro', 'situacao_atual')

@admin.register(Filho)
class FilhoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_nascimento', 'membro')
    search_fields = ('nome',)

