from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

class CalculoDieteticoView(TemplateView):
    template_name = 'calculo_dietetico/calculo_dietetico.html'
