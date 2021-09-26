from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from perfil.models import Usuario,Equipo

@login_required(login_url='login')
def felicidad(request):
    return render(
        request,
        'felicidad/Felicidad.html',
        {
        'nombreSeccion':'¿Como estan?'
        }
    )
