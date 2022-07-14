from django import forms

class ingresarForm(forms.Form):
    usuario= forms.CharField(max_length=50)
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    

class productoForm(forms.Form):
    nombre = forms.CharField(max_length=300)
    categoria = forms.CharField(max_length=32)
    precio = forms.FloatField()