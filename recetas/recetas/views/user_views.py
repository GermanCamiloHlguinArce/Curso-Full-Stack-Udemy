from django.shortcuts import render


def registro(request):
    contexto = {}
    return render(request, "registro.html", contexto)
