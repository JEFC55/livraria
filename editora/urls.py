from django.urls import path , include
from .views import listar_editoras, cadastrar_editora, atualizar_editora, excluir_editora
urlpatterns = [
    path('listar-editoras/', listar_editoras, name='listar_editoras'),
    path('cadastrar-editora/', cadastrar_editora, name='cadastrar_editora'),
    path('atualizar-editora/<int:editora_id>/', atualizar_editora, name='atualizar_editora'),
    path('excluir-editora/<int:editora_id>/', excluir_editora, name='excluir_editora'),
]