from django.db import models
from django.apps import apps

class PessoaDAO(models.Manager):
	def retorna_C(self):
		return self.filter(nome__startswith="C")

	def nova(nome, idade, cpf, logradouro, numero, bairro, cep):
		p = Pessoa(nome=nome, idade=idade, cpf = cpf)
		end = Endereco(pessoa=p,
			logradouro=logradouro, numero=numero,
			bairro=bairro, cep=cep)
		p.save()
		end.save()
		return p

class Pessoa(models.Model):
	nome = models.CharField(max_length=200)
	idade = models.IntegerField(default=0)
	cpf = models.CharField(max_length=14, null=True)

	def __str__(self):
		return f"{self.nome} (id={self.id})"

	"""def detalhar(self):
		result1 = Endereco.objects.get(pessoa__id=self.id)
		result2 = Conjuge.objects.get(pessoa__id=self.id)
		result3 = Automovel.objects.get(pessoa__id=self.id)

		result = {
			"conjuge": result2,
			"endereco": result1,
			"automovel": result3
			}

		if(result):
			return result"""

	def detalhar(self):
		result = Endereco.objects.get(pessoa__id=self.id)
		if(result):
			return result

	objects = PessoaDAO()


class Endereco(models.Model):
	pessoa = models.ForeignKey("Pessoa", on_delete=models.CASCADE)
	logradouro = models.CharField(max_length=200)
	numero = models.IntegerField()
	bairro = models.CharField(max_length=100,null=True)
	cep = models.CharField(max_length=9)
	
	def __str__(self):
		detalhe = f""" {self.logradouro}, n°: {self.numero}.
			Bairro {self.bairro}. CEP: {self.cep}
		"""
		return detalhe


#Exercício_2
class Aluno(models.Model):
	nome = models.CharField(max_length=200)
	idade = models.IntegerField(default=0)
	cpf = models.CharField(max_length=14, null=True)
	automovel = models.ForeignKey("Automovel", on_delete=models.CASCADE)
	conjuge = models.ForeignKey("Conjuge", on_delete=models.CASCADE)

	def __str__(self):
		#detalhe = f""" Nome: {self.nome}, Idade: {self.idade}, CPF: {self.cpf}, Automóvel: {self.automovel}, Conjuge: {self.conjuge}"""
		detalhe = f""" Nome: {self.nome}"""
		return detalhe

class Automovel(models.Model):
	modelo = models.CharField(max_length=200)
	marca = models.CharField(max_length=200)
	cor = models.CharField(max_length=200)
	
	def __str__(self):
		detalhe = f""" {self.modelo}, Marca: {self.marca}, Cor: {self.cor}"""
		return detalhe

class Conjuge(models.Model):
	nome = models.CharField(max_length=200)
	idade = models.IntegerField()
	
	def __str__(self):
		detalhe = f""" {self.nome}, Idade: {self.idade}"""
		return detalhe