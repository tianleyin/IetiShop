from django.contrib.auth.models import User
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    padre = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='child')

    def __str__(self):
        return self.nombre

class Tag(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, blank=True)
    cantidad_disponible = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)

class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_compra = models.DateTimeField(auto_now_add=True)  
    precio_total = models.DecimalField(max_digits=10,decimal_places=2)

class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10,decimal_places=2)
