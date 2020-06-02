from django.contrib import admin

# Register your models here.
from .models import Pessoa, Aluno, Endereco, Automovel, Conjuge

admin.site.register(Pessoa)
admin.site.register(Aluno)
admin.site.register(Endereco)
admin.site.register(Automovel)
admin.site.register(Conjuge)