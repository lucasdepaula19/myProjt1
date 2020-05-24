from django.urls import path

from .views import people_views as pv

urlpatterns = [
	path('', pv.home, name="index"),
	path('listar/', pv.listar, name="listar"),

	path('listar/inicia_com', pv.listar, name="inicia_com"),
	path('listar/termina_com', pv.listar, name="termina_com"),
	path('listar/contem', pv.listar, name="contem"),
	path('listar/nao_contem', pv.listar, name="nao_contem"),

	path('detalhar/<int:id_pessoa>/', pv.detalhar, name="detalhar"),
	path('excluir/<int:id_pessoa>/', pv.excluir, name="excluir"),
	path('cadastro/', pv.cadastro, name="cadastro"),
	path('cadastrar/', pv.cadastrar, name="cadastrar")
]