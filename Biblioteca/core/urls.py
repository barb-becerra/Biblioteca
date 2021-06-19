from django.urls import path
from .views import inicio, formulario, libros, form_libro

urlpatterns = [
    path('', inicio, name="inicio"),
    path('formulario', formulario, name="formulario"),
    path('libros', libros, name="libros"),
    path('addlibro', form_libro, name="form_libro"),
]

