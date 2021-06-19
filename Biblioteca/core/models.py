from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de la categoria')
    nombreCategoria = models.CharField(max_length = 50, verbose_name='Nombre de la Categoria')
    def __str__(self):
        return self.nombreCategoria
class Libro(models.Model):
    idISBN = models.IntegerField(primary_key=True, verbose_name='Id de ISBN')
    nombreLibro = models.CharField(max_length = 50, verbose_name='Nombre del Libro')
    autorLibro = models.CharField(max_length = 50, verbose_name='Nombre del Autor')
    descripcion = models.CharField(max_length = 100, verbose_name = 'Descripcion del libro')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.idISBN