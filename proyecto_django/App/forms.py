from django import forms
from .models import socios

class SociosForm (forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.CharField()
    email = forms.EmailField()
    telefono = forms.CharField()



class BuscaSocioForm(forms.Form):
    nombre = forms.CharField(required=False, label="Nombre", max_length=100)
    apellido = forms.CharField(required=False, label="Apellido", max_length=100)
    



