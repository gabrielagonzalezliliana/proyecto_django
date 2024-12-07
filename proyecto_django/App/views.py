from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Vista inicio")

def socios(request):
    return HttpResponse("vista socios")

def actividades(request):
    return HttpResponse("vista actividades")

def sucursales(request):
    return HttpResponse("vista sucursales")