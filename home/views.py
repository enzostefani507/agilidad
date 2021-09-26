from django.shortcuts import redirect, render
from django.http import HttpResponse

def home(request):
    return render(
        request,
        'home/inicio.html',
        {
        'nombreSeccion':'Saludos!'
        }
    )
    