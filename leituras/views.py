from django.shortcuts import render
from .models import AcessoRFID

def listar_acessos(request):
    acessos = AcessoRFID.objects.all().order_by('-data_hora')
    return render(request, 'leituras/listar.html', {'acessos': acessos})