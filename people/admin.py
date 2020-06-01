from django.contrib import admin

# Register your models here.
from .models import Pessoa, Endereco, Automovel, Conjuge

admin.site.register(Pessoa)
admin.site.register(Endereco)
admin.site.register(Automovel)
admin.site.register(Conjuge)