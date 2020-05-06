from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="index"),
    path('listar', views.listar, name="listar"),
    path('detalhar/<int:id_pessoa>/', views.detalhar, name="detalhar"),
    path('excluir/<int:id_pessoa>/', views.excluir, name="excluir")
]