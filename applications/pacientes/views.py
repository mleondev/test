from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from .models import Pacientes
from . import forms

# Template de Pruebas
class PruebaView(TemplateView):
    template_name = 'prueba.html'

# Templates del Proyecto
class InicioView(TemplateView):
    template_name = 'inicio.html'

class RegistrarPacientes(CreateView):
    model = Pacientes
    form_class = forms.FormPacientes
    template_name = 'pacientes/registro_pacientes.html'
    success_url = reverse_lazy('pacientes:registrado_pacientes')

class RegistradoPacientes(TemplateView):
    template_name = 'pacientes/registrado_pacientes.html'

class ListaPacientes(ListView):
    model = Pacientes
    template_name = 'pacientes/lista_pacientes.html'
    paginate_by = 4
    

    # Esta funcion genera el contexto (las variables que entran al template)
    def get_context_data(self, **kwargs):
        context = {}
        paciente_buscado = self.request.GET.get('paciente_buscado')
        if paciente_buscado is not None:
            context['lista_pacientes'] = Pacientes.objects.filter(activo=True, nombre__icontains=paciente_buscado)
        else:
            context['lista_pacientes'] = Pacientes.objects.filter(activo=True)
        return context

    # Esta funcion define lo que a a pasar cuando se ejecute el metodo GET
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    # Esta funcion define lo que va a pasar cuando se ejectute el metodo POST
    def post(self, request, *args, **kwargs):
        id_pacientes_eliminar = request.POST.getlist('pacientes_marcados')
        pacientes_eliminar = self.model.objects.filter(id__in=id_pacientes_eliminar)
        for pacientes in pacientes_eliminar:
            pacientes.activo = False
        print('antes del update')
        self.model.objects.bulk_update(pacientes_eliminar, ['activo'])
        return redirect('pacientes:lista_pacientes')



class ConsultaPacientes(DetailView):
    model = Pacientes
    template_name = 'pacientes/consulta_pacientes.html'