from ast import Return
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from AppCarrito.forms import ingresarForm, productoForm

# Create your views here.

def inicio(request):
    return render(request, 'AppCarrito/inicio.html')

def producto(request):
    return render(request, 'AppCarrito/producto.html')

def ingresar(request):
    return render(request, 'AppCarrito/ingresar.html')   

def carrito(request):
    return render(request, 'AppCarrito/carrito.html')

def ingresarFormulario(request):
    return render(request, 'AppCarrito/ingresarFormulario.html')    


def ingresarForm(request):
    
    if (request.method=="POST"):
        form= ingresarForm(request.POST)
        print(form)
        if form.is_valid():
            info= form.cleaned_data
            print(info)
            usuario= info["usuario"]
            nombre= info["nombre"]
            apellido= info["apellido"]
            email=  info["email"]
            ingresar= ingresar(usuario=usuario, nombre=nombre, apellido=apellido, email=email)
            ingresar.save()
            return render (request, "AppCarrito/inicio.html")
    else:
        form= ingresarForm()
    return render(request, "AppCarrito/ingresarFormulario.html", {"formulario":form})         

def productoFormulario(request):

    if (request.method=="POST"):
        form= productoForm(request.POST)
        print(form)
        if form.is_valid():
            info= form.cleaned_data
            nombre= info["nombre"]
            categoria= info["categoria"]
            precio= info["precio"]
            producto= producto(nombre=nombre, categoria=categoria, precio=precio)
            producto.save()
            return render (request, "AppCarrito/inicio.html")
    else:
        form= productoForm()
    return render(request, "AppCarrito/productoFormulario.html", {"formulario":form}) 


def busquedaProductos(request):
    return render(request, 'AppCarrito/busquedaProductos.html')


def buscar(request):
    if request.GET["producto"]:
        produ= request.GET["producto"]
        productos= producto.objects.filter(producto=produ)
        return render(request, 'AppCarrito/resultadosBusqueda.html', {"producto":producto})
    else:
        return render(request, 'AppCarrito/busquedaProductos.html', {"error":"No se ingreso ningun producto"})



def miCuenta(request):
    return render(request, 'AppCarrito/miCuenta.html')