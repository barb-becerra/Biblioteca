from django.shortcuts import render
from .models import Libro
#from .forms import LibroForm

# Create your views here.
def inicio(request):
    return render(request, 'core/home.html')
    
def formulario(request):
    return render(request, 'core/formulario.html')

def libros(request):
    libros = Libro.objects.all()
    datos = {
        'libros' : libros
    }
    return render(request, 'core/libros.html', datos)

def form_libro(request):
    return render(request, 'core/addlibro.html')

