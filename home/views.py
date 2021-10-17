from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *

def home(request):
    temas = Tema.objects.all()
    unidades = Unidad.objects.all()
    context ={
        'nombreSeccion':'Saludos!',
        'contenido': temas,
        'unidades':unidades
    }
    return render(request,'home/inicio.html',context)
    