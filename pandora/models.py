from django.db import models

# Create your models here.

class Amigurumis(models.Model):

    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='amigurumis/')
    categoria = models.CharField(max_length=50)
    subcategoria = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    descripcion = models.TextField()

    def __str__(self):
        return f'{self.nombre} - {self.categoria} - {self.subcategoria}'
    
class Ropa(models.Model):

    nombre = models.CharField(max_length=50)
    imagen = models.ImageField()
    categoria = models.CharField(max_length=50)
    subcategoria = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    descripcion = models.TextField()

    def __str__(self):
        return f'{self.nombre} - {self.categoria} - {self.subcategoria}'

class Insumos(models.Model):

    nombre = models.CharField(max_length=50)
    imagen = models.ImageField()
    categoria = models.CharField(max_length=50)
    subcategoria = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    descripcion = models.TextField()

    def __str__(self):
        return f'{self.nombre} - {self.categoria} - {self.subcategoria}'