from ast import Return
from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.

def inicio(request):
    return render(request, 'AppCarrito/inicio.html')

def producto(request):
    return render(request, 'AppCarrito/producto.html')

def ingresar(request):
    return render(request, 'AppCarrito/ingresar.html')   

def carrito(request):
    return render(request, 'AppCarrito/carrito.html')

