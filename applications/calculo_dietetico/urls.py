from django.contrib import admin
from django.urls import path
from .views import *
from . import views

app_name = 'calculo_dietetico'

# Establecemos las URL de esta view
urlpatterns = [
    path('calculo-dietetico/', CalculoDieteticoView.as_view(), name='calculo'),
]