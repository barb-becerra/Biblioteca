from django.urls import path
from .views import inicio, formulario, libros, form_libro, form_mod_libro, form_del_libro

urlpatterns = [
    path('', inicio, name="inicio"),
    path('registro', formulario, name="formulario"),
    path('libros', libros, name="libros"),
    path('addlibro', form_libro, name="form_libro"),
    path('mod_libro/<id>', form_mod_libro, name="mod_libro"),
    path('del_libro/<id>', form_del_libro, name="del_libro"),
]

