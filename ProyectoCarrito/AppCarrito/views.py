from ast import Return
from django.http import HttpResponse
from django.shortcuts import render
from .models import tienda

# Create your views here.

def inicioApp(request):
    return render(request, 'AppCarrito/inicio.html')

def tienda(request):
    tienda.save()
    return render(request, 'AppCarrito/tienda.html')