from django.urls import path

from .views import people_views as pv

urlpatterns = [
	path('', pv.home, name="index"),
	path('listar/', pv.listar, name="listar"),

	path('listar/inicia_com/<letra_pessoa>/', pv.inicia_com, name="inicia_com"),
	path('listar/termina_com/<letra_pessoa>/', pv.termina_com, name="termina_com"),
	path('listar/contem/<letra_pessoa>/', pv.contem, name="contem"),
	path('listar/nao_contem/<letra_pessoa>/', pv.nao_contem, name="nao_contem"),

	path('detalharAluno/<int:id_aluno>/', pv.detalharAluno, name="detalharAluno"),
	path('excluirAluno/<int:id_aluno>/', pv.excluirAluno, name="excluirAluno"),

	path('detalharAutomovel/<int:id_automovel>/', pv.detalharAutomovel, name="detalharAutomovel"),
	path('excluirAutomovel/<int:id_automovel>/', pv.excluirAutomovel, name="excluirAutomovel"),

	path('detalharConjuge/<int:id_conjuge>/', pv.detalharConjuge, name="detalharConjuge"),
	path('excluirConjuge/<int:id_conjuge>/', pv.excluirConjuge, name="excluirConjuge"),

	path('detalhar/<int:id_pessoa>/', pv.detalhar, name="detalhar"),
	path('excluir/<int:id_pessoa>/', pv.excluir, name="excluir"),
	
	path('cadastro/', pv.cadastro, name="cadastro"),
	path('cadastrar/', pv.cadastrar, name="cadastrar"),

	path('criarAutomovel/', pv.criar_automovel, name="criar_automovel"),
	path('criarAluno/', pv.criar_aluno, name="criar_aluno"),
	path('criarConjuge/', pv.criar_conjuge, name="criar_conjuge"),

	path('listarAutomovel/', pv.listar_automovel, name="listar_automovel"),
	path('listarAluno/', pv.listar_aluno, name="listar_aluno"),
	path('listarConjuge/', pv.listar_conjuge, name="listar_conjuge")
]