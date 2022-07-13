from django.contrib import admin
from .models import carrito, producto, ingresar

# Register your models here.

admin.site.register(carrito)
admin.site.register(ingresar)
admin.site.register(producto)
