from django.shortcuts import render, redirect
from .models import Libro
from .forms import LibroForm

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
    datos = {
        'form' : LibroForm()
    }
    if request.method=="POST":
        formulario = LibroForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Libro Agregado"

    return render(request, 'core/addlibro.html', datos)
    redirect(to="libros")

def form_mod_libro(request, id):
    libro = Libro.objects.get(idISBN=id)
    datos = {
        'form' : LibroForm(instance=libro)
    }
    if request.method == 'POST':
        formulario = LibroForm(data=request.POST, instance=libro)
        if formulario.is_valid:
            formulario.save()
        datos['mensaje'] = "Libro Modificado"
    return render(request, 'core/modlibro.html', datos)

def form_del_libro (request, id):
    libro = Libro.objects.get(idISBN = id)
    libro.delete()
    return redirect(to="libros")