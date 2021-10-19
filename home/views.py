from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from perfil.models import Usuario
def home(request):
    temas = Tema.objects.all()
    unidades = Unidad.objects.all()
    ranking = Usuario.objects.filter(dorado__gt=0).order_by('dorado').reverse()
    context ={
        'nombreSeccion':'Saludos!',
        'contenido': temas,
        'unidades':unidades,
        'ranking': ranking
    }
    return render(request,'home/inicio.html',context)
    