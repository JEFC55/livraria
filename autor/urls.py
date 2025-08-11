from autor.views import listar_autores, cadastrar_autor, atualizar_autor, excluir_autor
from django.urls import path
urlpatterns = [
    path('listar-autores/', listar_autores, name='listar_autores'),
    path('cadastrar-autor/', cadastrar_autor, name='cadastrar_autor'),
    path('atualizar-autor/<int:autor_id>/', atualizar_autor, name='atualizar_autor'),
    path('excluir-autor/<int:autor_id>/', excluir_autor, name='excluir_autor'),
]