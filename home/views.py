from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from perfil.models import Usuario, Equipo
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    temas = Tema.objects.all()
    unidades = Unidad.objects.all()
    ranking_personas = Usuario.objects.filter(dorado__gt=0).order_by('dorado').reverse()
    ranking_equipos = Equipo.objects.all().order_by('puntos').reverse()
    context ={
        'nombreSeccion':'Saludos!',
        'contenido': temas,
        'unidades':unidades,
        'ranking_personas': ranking_personas,
        'ranking_equipos': ranking_equipos
    }
    return render(request,'home/inicio.html',context)
    