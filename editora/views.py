from django.shortcuts import render
from .models import Editora
from django.http import HttpRequest, JsonResponse
import json
def listar_editoras(request):
    if request.method == "GET":
        nome = request.GET.get("nome", "")
        editoras = Editora.objects.all()
        if nome:
            editoras = editoras.filter(nome__icontains=nome)
        return JsonResponse({"editoras": [editora.to_dict() for editora in editoras]})

def cadastrar_editora(request:HttpRequest):
    if request.method == "POST":
        try:
            data:dict = json.loads(request.body)
            editora = Editora(**data)
            editora.clean()
            editora.save()
            return JsonResponse({"id": editora.id}, status=201)
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)
def atualizar_editora(request:HttpRequest, editora_id:int):
    if request.method == "PUT":
        try:
            data:dict = json.loads(request.body)
            editora = Editora.objects.get(id=editora_id)
            for key, value in data.items():
                setattr(editora, key, value)
            editora.clean()
            editora.save()
            return JsonResponse({"id": editora.id}, status=200)
        except Editora.DoesNotExist:
            return JsonResponse({"error": "Editora não encontrada."}, status=404)
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)

def excluir_editora(request:HttpRequest, editora_id:int):
    if request.method == "DELETE":
        try:
            editora = Editora.objects.get(id=editora_id)
            editora.delete()
            return JsonResponse({"message": "Editora excluída com sucesso."}, status=204)
        except Editora.DoesNotExist:
            return JsonResponse({"error": "Editora não encontrada."}, status=404)