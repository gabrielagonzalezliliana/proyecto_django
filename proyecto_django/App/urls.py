
from django.urls import path
from App import views

urlpatterns = [
    path("", views.inicio, name = "inicio"),
    path("socios/", views.socios, name = "socios"),
    path("actividades/", views.actividades, name = "actividades"),
    path("sucursales/", views.sucursales, name = "sucursales")
]
