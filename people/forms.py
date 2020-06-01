from django import forms
from .models import Pessoa, Endereco, Automovel, Conjuge

class AutomovelForm(forms.ModelForm):
    class Meta:
        model = Automovel
        fields = ['pessoa','modelo', 'marca', 'cor']
