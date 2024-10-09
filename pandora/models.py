from django.db import models
from django.contrib.auth.models import User

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
    
class Avatar(models.Model):

  user = models.ForeignKey(User, on_delete=models.CASCADE)
  imagen = models.ImageField(upload_to='avatares', blank=True, null=True)


class Carrito(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    amigurumi = models.ForeignKey(Amigurumis, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.amigurumi.nombre} - Cantidad: {self.cantidad}'