from django.shortcuts import render
from .models import Autor
from django.http import JsonResponse, HttpResponse, HttpRequest
import json

def listar_autores(request:HttpRequest):
    if request.method == "GET":
        nome = request.GET.get("nome", "")
        autores = Autor.objects.all()
        if nome:
            autores = autores.filter(nome__icontains=nome)
        return JsonResponse({"autores": [autor.to_dict() for autor in autores]})

def cadastrar_autor(request:HttpRequest):
    if request.method == "POST":
        try:
            data: dict = json.loads(request.body)
            autor = Autor(**data)
            autor.clean()
            autor.save()
            return JsonResponse({"id":autor.id}, status=201)
        except Exception as e:
            return JsonResponse({"error":str(e)}, status=400)
        
def atualizar_autor(request:HttpRequest, autor_id:int):
    if request.method == "PUT":
        try:
            dados: dict = json.loads(request.body)
            autor: Autor = Autor.objects.get(id=autor_id)
            for chave, valor in dados.items():
                setattr(autor, chave, valor)
            autor.clean()
            autor.save()
            return JsonResponse(autor.to_dict(), status=200)
        except Autor.DoesNotExist:
            return JsonResponse({"error": "Autor não encontrado"}, status=404)
        except Exception as e:
            return JsonResponse({"error": f"Erro ao atualizar o autor. Verifique a solicitação! {str(e)}"}, status=500)
        
def excluir_autor(request:HttpRequest, autor_id:int):
    if request.method == "DELETE":
        try:
            autor: Autor = Autor.objects.get(id=autor_id)
            autor.delete()
            return JsonResponse({"message":"Autor excluído com sucesso!"}, status=204)
        except Autor.DoesNotExist:
            return JsonResponse({"error": "Autor não encontrado"}, status=404)
        except Exception as e:
            return JsonResponse({"error": f"Erro ao excluir o autor. Verifique a solicitação! {str(e)}"}, status=500)