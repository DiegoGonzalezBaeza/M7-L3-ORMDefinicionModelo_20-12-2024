from django.shortcuts import render, redirect
from .models import Estudiante
from .forms import EstudianteForm
from django.http import JsonResponse

# Create your views here.

# Vista para la página de inicio
def index(request):
    return render(request, 'gestion_alumnos/index.html')

# Vista para listar estudiantes
def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'gestion_alumnos/lista_estudiantes.html', {'estudiantes': estudiantes})

# Vista para agregar un estudiante
def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')
    else:
        form = EstudianteForm()
    return render(request, 'gestion_alumnos/crear_estudiante.html', {'form': form})

# Vista para seleccionar un estudiante
def detalles_estudiante(request, id):
    estudiante = Estudiante.objects.get(id=id)
    return render(request, 'gestion_alumnos/detalles_estudiante.html', {'estudiante': estudiante})

# Vista para buscar estudiantes por nombre o apellido
def buscar_estudiante(request):
    query = request.GET.get('q', '')
    estudiantes = Estudiante.objects.filter(nombre__icontains=query) | Estudiante.objects.filter(apellido__icontains=query)
    resultados = list(estudiantes.values('id', 'nombre', 'apellido', 'email'))
    return JsonResponse({'resultados': resultados})