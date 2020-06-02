from django import forms
from .models import Pessoa, Aluno, Endereco, Automovel, Conjuge

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome','idade','cpf','automovel', 'conjuge']

class AutomovelForm(forms.ModelForm):
    class Meta:
        model = Automovel
        fields = ['modelo', 'marca', 'cor']

class ConjugeForm(forms.ModelForm):
    class Meta:
        model = Conjuge
        fields = ['nome','idade']