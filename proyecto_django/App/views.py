from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def inicio(request):
    return render(request, "App/inicio.html")

def socios(request):
    return render(request,"App/socios.html")

def actividades(request):
    return render(request,"App/actividades.html")

def sucursales(request):
    return render(request,"App/sucursales.html")