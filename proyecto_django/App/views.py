from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def inicio(request):
    return render(request, "App/inicio.html")

def ver_socios(request):
    return render(request,"App/socios.html")

def actividades(request):
    return render(request,"App/actividades.html")

def sucursales(request):
    return render(request,"App/sucursales.html")

from App.models import socios
from App.forms import SociosForm
from App.forms import BuscaSocioForm

def socios_formulario(request):
    if request.method == 'POST':
        form = SociosForm(request.POST)

        if form.is_valid():
            informacion = form.cleaned_data

            nuevo_socio = socios(nombre=informacion["nombre"], apellido=informacion["apellido"], dni=informacion["dni"], email=informacion["email"], telefono=informacion["telefono"])
            nuevo_socio.save()

            return render(request, "App/inicio.html")
    else:
        form= SociosForm()

    return render(request, 'App/socios_formulario.html', {'form': form})



def buscar_socio(request):
    if request.method == "POST":
        mi_formulario = BuscaSocioForm(request.POST)  # Aquí recibimos los datos del formulario

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            # Buscar socios según los datos ingresados en el formulario
            socios_filtrados = socios.objects.all()

            if informacion.get("nombre"):
                socios_filtrados = socios_filtrados.filter(nombre__icontains=informacion["nombre"])

            if informacion.get("apellido"):
                socios_filtrados = socios_filtrados.filter(apellido__icontains=informacion["apellido"])

            return render(request, "App/mostrar_socios.html", {"socios": socios_filtrados})
    else:
        mi_formulario = BuscaSocioForm()

    return render(request, "App/buscar_socio.html", {"mi_formulario": mi_formulario})


