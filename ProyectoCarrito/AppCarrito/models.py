from ast import Return
from django.db import models

# Create your models here.

class producto(models.Model):
    nombre = models.CharField(max_length=300)
    categoria = models.CharField(max_length=32)
    precio = models.FloatField()

def __str__(self):
    return self.nombre




class ingresar(models.Model):
    usuario= models.CharField(max_length=50)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

def __str__(self):
    return f'{self.nombre} -> {self.apellido}'





class carrito(models.Model):
    
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"]={}
            self.carrito = carrito
       
def __str__(self):
    return f'{self.nombre} -> {self.precio}'       