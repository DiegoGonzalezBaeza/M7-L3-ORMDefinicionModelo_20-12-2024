from django import forms
from .models import Estudiante

# Una buena practica es crear el formulario con el siguiente nombre:
# NombreModeloForm

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'email', 'promedio']


# class EstudianteForm(forms.ModelForm):
#     class Meta:
#         model = Estudiante
#         fields = '__all__'
#         labels = {
#             'nombre': 'Nombre',
#             'apellido': 'Apellido',
#             'fecha_nacimiento': 'Fecha de Nacimiento',
#             'email': 'Correo Electrónico',
#             'promedio': 'Promedio',
#         }
#         widgets = {
#             'nombre': forms.TextInput(attrs={'class': 'form-control'}),
#             'apellido': forms.TextInput(attrs={'class': 'form-control'}),
#             'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'promedio': forms.NumberInput(attrs={'class': 'form-control'}),
#         }