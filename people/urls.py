from django.urls import path

from .views import people_views as pv

urlpatterns = [
	path('', pv.home, name="index"),
	path('listar/', pv.listar, name="listar"),

	path('listar/inicia_com/<letra_pessoa>/', pv.inicia_com, name="inicia_com"),
	path('listar/termina_com/<letra_pessoa>/', pv.termina_com, name="termina_com"),
	path('listar/contem/<letra_pessoa>/', pv.contem, name="contem"),
	path('listar/nao_contem/<letra_pessoa>/', pv.nao_contem, name="nao_contem"),

	path('detalhar/<int:id_pessoa>/', pv.detalhar, name="detalhar"),
	path('excluir/<int:id_pessoa>/', pv.excluir, name="excluir"),
	path('cadastro/', pv.cadastro, name="cadastro"),
	path('cadastrar/', pv.cadastrar, name="cadastrar")
]