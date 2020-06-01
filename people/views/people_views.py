from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader
from django.shortcuts import render
from datetime import datetime
from ..models import Pessoa, Endereco, Automovel, Conjuge
from ..forms import AutomovelForm

@require_http_methods(["GET","POST"])
def home(request):
	return HttpResponse("Olá, requisição feita com sucesso!")

@csrf_exempt
@require_http_methods(["POST","GET"])
def listar(request):
	result = Pessoa.objects.all()
	#result = Pessoa.objects.retorna_C()
	template = loader.get_template('listar.html')
	context = {
		'lista' : result,
	}
	return HttpResponse(template.render(context, request))

def detalhar(request, id_pessoa):
	pessoa = Pessoa.objects.get(id=id_pessoa)
	context = {'pessoa':pessoa}
	return render(request, 'detalhe.html', context)

def excluir(request, id_pessoa):
	try:
		pessoa = Pessoa.objects.get(id=id_pessoa)
		pessoa.delete()		
		return HttpResponse(f"Excluiu {pessoa.nome} (id={pessoa.id})")
	except ObjectDoesNotExist:
		return HttpResponse("Pessoa não encontrada")

def cadastro(request):
	"""sexos = ['Masculino','Feminino']
	template = loader.get_template('cadastrar.html')
	context = {
		'sexos': sexos,
	}
	return HttpResponse(template.render(context, request))"""

	context = {
	}
	template = loader.get_template('cadastrar.html')
	return HttpResponse(template.render(context, request))

def cadastrar(request):
	p = Pessoa.objects.nova(request.POST['nome'], request.POST['idade'], request.POST['cpf'], request.POST['logradouro'], request.POST['numero'], request.POST['bairro'], request.POST['cep'])
	return HttpResponse(f"{p} cadastrado com sucesso")



#Exercício_3
def inicia_com(request, letra_pessoa):
	result = Pessoa.objects.filter(nome__startswith=letra_pessoa)
	template = loader.get_template('listar.html')
	context = {
		'lista' : result,
	}
	return HttpResponse(template.render(context, request))

def termina_com(request, letra_pessoa):
	result = Pessoa.objects.filter(nome__endswith=letra_pessoa)
	template = loader.get_template('listar.html')
	context = {
		'lista' : result,
	}
	return HttpResponse(template.render(context, request))

def contem(request, letra_pessoa):
	result = Pessoa.objects.filter(nome__contains=letra_pessoa)
	template = loader.get_template('listar.html')
	context = {
		'lista' : result,
	}
	return HttpResponse(template.render(context, request))

def nao_contem(request, letra_pessoa):
	result = Pessoa.objects.exclude(nome__contains=letra_pessoa)
	template = loader.get_template('listar.html')
	context = {
		'lista' : result,
	}
	return HttpResponse(template.render(context, request))


#exercício_4
@csrf_exempt
@require_http_methods(["POST","GET"])
def criar_automovel(request):
	form2 = AutomovelForm(request.POST or None)

	"""if(form.is_valid()):
		form.save()
		return redirect('listar')

	return render(request, 'automovel-form.html', {'form', form})"""

	context = {
		'form': AutomovelForm(request.POST or None),
	}

	if(form2.is_valid()):
		form2.save()
		return redirect('listar')

	template = loader.get_template('automovel-form.html')
	return HttpResponse(template.render(context, request))