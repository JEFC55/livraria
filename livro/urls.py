from django.urls import path
from .views import listar_livros, cadastrar_livro, atualizar_livro, excluir_livro
urlpatterns = [
    path(route='listar-livros/', view=listar_livros, name='listar_livros'),
    path('cadastrar-livro/', cadastrar_livro, name='cadastrar_livro'),
    path('cadastrar-livro/<int:autor_id>/', cadastrar_livro, name='cadastrar_livro_autor'),
    path('atualizar-livro/<int:livro_id>/', atualizar_livro, name='atualizar_livro'),
    path('excluir-livro/<int:livro_id>/', excluir_livro, name='excluir_livro'),
]