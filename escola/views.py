from django.http import HttpRequest, JsonResponse


def estudantes(request: HttpRequest):
    if request.method == "GET":
        estudante = {"id": 1, "nome": "Eu"}
        return JsonResponse(estudante)

    return JsonResponse({})
