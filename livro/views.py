import json
from typing import List #estudar
from django.http import HttpRequest, JsonResponse

from autor.models import Autor
from editora.models import Editora
from livro.models import Livro

def listar_livros(request: HttpRequest):
    if request.method == "GET":
        titulo = request.GET.get("titulo", "")
        livros = Livro.objects.all()
        if titulo:
            livros = livros.filter(titulo__icontains=titulo)
        return JsonResponse({"livros": [livro.to_dict() for livro in livros]})
    
def cadastrar_livro(request: HttpRequest, autor_id:int = None):
    if request.method == "POST":
        try:
            if autor_id:
                autor = Autor.objects.get(id=autor_id)
                data: dict = json.loads(request.body)
                livro = Livro(**data, autor=autor)
                livro.clean()
                livro.save()
                context = {
                    "autor":[autor.to_dict()],
                    "message": f"Livro '{livro.titulo}' cadastrado com sucesso. Autor: {autor.nome}",
                }
                return JsonResponse(context, status=201)
            else:
                data: dict =json.loads(request.body)
                autor = Autor.objects.get(id=data["autor"])
                data.pop("autor")
                editora = Editora.objects.get(id=data["editora"])
                data.pop("editora")
                livro = Livro(**data, autor=autor, editora=editora)
                livro.clean()
                livro.save()
                return JsonResponse({"id":livro.id}, status=201)
        except Exception as e:
            return JsonResponse({"error":str(e)}, status=400)
        
def atualizar_livro(request: HttpRequest, livro_id: int):
    if request.method == "PUT":
        try:
            data: dict = json.loads(request.body)
            livro = Livro.objects.get(id=livro_id)
            for key, value in data.items():
                setattr(livro, key, value)
            livro.clean()
            livro.save()
            return JsonResponse(livro.to_dict(), status=200)
        except Livro.DoesNotExist:
            return JsonResponse({"error": "Livro não encontrado"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500) 
         
def excluir_livro(request: HttpRequest, livro_id: int):
    if request.method == "DELETE":
        try:
            livro = Livro.objects.get(id=livro_id)
            livro.delete()
            return JsonResponse({"message": "Livro excluído com sucesso"}, status=204)
        except Livro.DoesNotExist:
            return JsonResponse({"error": "Livro não encontrado"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)