from tkinter import Widget
from django import forms
from applications.pacientes.models import Pacientes

class FormPacientes(forms.ModelForm):
    class Meta:
        model = Pacientes

        fields = ('codigo','nombre','email','sexo','fecha_nacimiento','escolaridad','tipo_sangre','estado_civil')

        widgets = {
            'codigo':forms.TextInput(
                attrs={
                    'placeholder':'Codigo',
                    'class':'input_registrar'
                }
            ),
            'nombre':forms.TextInput(
                attrs={
                    'placeholder':'Nombre',
                    'class':'input_registrar'
                }
            ),
            'email':forms.TextInput(
                attrs={
                    'placeholder':'Email',
                    'class':'input_registrar'
                }
            ),
            'sexo': forms.TextInput(
                attrs={
                    'placeholder':'Sexo',
                    'class':'input_registrar'
                }
            ),
            'fecha_nacimiento': forms.DateInput(
                attrs={
                    'placeholder':'Fecha de Nacimiento',
                    'class':'input_registrar'
                }
            ),
            'escolaridad': forms.TextInput(
                attrs={
                    'placeholder':'Escolaridad',
                    'class':'input_registrar'
                }
            ),
            'tipo_sangre': forms.TextInput(
                attrs={
                    'placeholder':'Tipo de Sangre',
                    'class':'input_registrar'
                }
            ),
            'estado_civil': forms.TextInput(
                attrs={
                    'placeholder':'Estado Civil',
                    'class':'input_registrar'
                }
            ),
        }