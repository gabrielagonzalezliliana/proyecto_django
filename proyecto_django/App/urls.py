
from django.urls import path
from App import views

urlpatterns = [
    path("", views.inicio, name = "inicio"),
    path("socios/", views.ver_socios, name = "socios"),
    path("actividades/", views.actividades, name = "actividades"),
    path("sucursales/", views.sucursales, name = "sucursales")
]

forms_api = [
    path('socios-formulario/', views.socios_formulario, name='socios_formulario'),
    path('buscar-socio/', views.buscar_socio, name="buscar_socio")
]

urlpatterns += forms_api