from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET","POST"])
def home(request):
    return HttpResponse("Olá, requisição feita com sucesso!")

def listar(request):
    return HttpResponse("<ul><li>Primeiro</li></ul>")

def detalhar(request, id_pessoa):
        return HttpResponse(f"Detalhou {id_pessoa}")

def excluir(request, id_pessoa):
        return HttpResponse(f"Excluiu {id_pessoa}")