from django.urls import path
from .views import index, lista_estudiantes, crear_estudiante, buscar_estudiante, detalles_estudiante

urlpatterns = [
    path('index/', index, name='index'),
    path('estudiantes/', lista_estudiantes, name='lista_estudiantes'),
    path('estudiantes/nuevo/', crear_estudiante, name='crear_estudiante'),
    path('estudiantes/detalles/<int:id>/', detalles_estudiante, name='detalles_estudiante'),
    path('estudiantes/buscar/', buscar_estudiante, name='buscar_estudiante'),
]