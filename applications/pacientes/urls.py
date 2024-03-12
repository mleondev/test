from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'pacientes'

# Establecemos las URL de esta view
urlpatterns = [
    path('prueba/', PruebaView.as_view(), name='prueba'),
    path('inicio/', InicioView.as_view(), name='inicio'),
    path('registro-pacientes/', RegistrarPacientes.as_view(), name='registro_pacientes'),
    path('registrado-pacientes/', RegistradoPacientes.as_view(), name='registrado_pacientes'),
    path('lista-pacientes/', ListaPacientes.as_view(), name='lista_pacientes'),
    path('consulta-pacientes/<int:pk>', ConsultaPacientes.as_view(), name='consulta_pacientes'),
]