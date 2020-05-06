from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_Length=200)
    idade = models.IntegerField(default=0)
    data_nascimento = models.DataField(null=True)
    cpf = models.CharField(max_Length=14, null=True)

class Endereco(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    logradouro = models.CharField(max_Length=200)
    numero = models.IntegerField()
    cep = models.CharField(max_Length=9)

class Departamento(models.Model):

class Cargo(models.Model):