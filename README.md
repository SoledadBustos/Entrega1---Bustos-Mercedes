# ProyectoCarrito

Creamos éste proyecto con el objetivo de ser la tienda preferida de los consumidores en productos, fundamentalmente alimenticios, a través de nuestra plataforma e-commerce.

Ser un supermercado moderno y de calidad, donde el cliente elige en libertad y donde buscamos la satisfacción continua de nuestros clientes a través de una atención y servicio que excede sus expectativas y una adaptación continua a sus necesidades.

## Requerimientos Técnicos

Se necesita tener instalado:
Visual Studio Code
Python
Django
Git

## Ejemplos

## Ejemplos
Si en la terminal hacemos
PS C:\Users\Usuario\Desktop\CoderDesafio\ProyectoCarrito\ProyectoCarrito> python manage.py runserver
vamos a dirigirnos al link http://127.0.0.1:8000/ donde veras nuestro CHANGUITO TIENDA ONLINE

Vas a encontrar 4 menus llamados 
- Productos
- Ingresar
- Carrito
- Mi cuenta

Por ejemplo para ingresar al menu Producto basta con hacer click en el boton llamado asi que te dirigira al link http://127.0.0.1:8000/AppCarrito/producto/ donde 
vas a ver las ofertas semanales disponibles.


Ademas, tenemos formularios que accedes a ellos colocando la siguiente ruta:

- http://127.0.0.1:8000/AppCarrito/productoFormulario/

- http://127.0.0.1:8000/AppCarrito/busquedaProductos/

y a nuestro panel de administracion accedes ingresando a la siguiente ruta:
- http://127.0.0.1:8000/admin/
En el tenemos 3 usuarios creados.
Ejemplo: usuario:maximiliano@gonzalez.com 
	     contras: admin

# Create your models here.

class producto(models.Model):
    nombre = models.CharField(max_length=300)
    categoria = models.CharField(max_length=32)
    precio = models.FloatField()
```


## Screenshots

![Ofertas](https://www.google.com.ar/search?sa=G&hl=es_419&tbs=simg:CAQSlwIJ_1CAD1zWBPJ4aiwILELCMpwgaOgo4CAQSFL4shA_1QPaAczBbPE6ES8AbVPYkNGhp5TwyCSCP9HaItVXpIXMeAj-eOalYLtBnkKSAFMAQMCxCOrv4IGgoKCAgBEgROHXD0DAsQne3BCRqrAQopChZhZHZhbmNlZCBtZWF0IHJlY292ZXJ52qWI9gMLCgkvbS8wMjg3d24KIgoPc2FsdC1jdXJlZCBtZWF02qWI9gMLCgkvbS8wNDdrYm0KHQoKYW5pbWFsIGZhdNqliPYDCwoJL20vMDE5dDZkCh4KC2Zyb3plbiBmb29k2qWI9gMLCgkvbS8wMXh4dG0KGwoIcmVkIG1lYXTapYj2AwsKCS9tLzA1djFxNww&sxsrf=ALiCzsZhtZNVLQgkwgLJVMyieiL2EPB9JQ:1657842505272&q=prote%C3%ADnas+del+estroma+de+la+carne&tbm=isch&ved=2ahUKEwiG0vrMyPn4AhUGupUCHe-lC-QQwg4oAHoECAEQNA&biw=1536&bih=746&dpr=1.25#imgrc=bTlzVvq1SLOtaM)
 
## Lessons Learned

Aprendimos a dominar herramientas básicas de la programación a través de Python. 
Pasamos por conceptos y comandos como diccionarios hasta 
En ésta ocasión aplicamos funcionalidades avanzadas como Django y Git. 

## Authors

- [@MaximilianoGonzalez23] (https://github.com/MaximilianoGonzalez23)

- [@SoledadBustos] (https://github.com/SoledadBustos)

- [@Melody-exe] (https://github.com/Melody-exe)

