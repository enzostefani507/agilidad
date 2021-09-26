from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from perfil.models import Usuario,Equipo
from estado.models import cambios
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse

class estado(LoginRequiredMixin,ListView):
    model = Equipo
    template_name = 'estado/Estado.html'
    context_object_name = 'equipo_list'
    login_url = '/perfil/login/'

    def get_context_data(self, **kwargs):
        context = super(estado, self).get_context_data(**kwargs)
        context['alumnos'] = Usuario.objects.all()
        context['nombreSeccion']='¿Como estamos?'
        user = Usuario.objects.filter(pk=self.request.user.id).first()
        context['perfil'] = user
        return context

def transferir_azul(request,origen_pk,destino_pk):
    orig = Usuario.objects.get(pk=origen_pk)
    des = Usuario.objects.get(pk=destino_pk)
    if origen.gris_disponible:
        nuevo_cambio = cambios(tipo='azul',origen=orig,destino=des)
        nuevo_cambio.save()
        orig.gris_disponible = False
        orig.save()    
        des.azul += 1
        des.save()
    return redirect('estado')


def transferir_dorado(request,origen_pk,destino_pk):
    orig = Usuario.objects.get(pk=origen_pk)
    des = Usuario.objects.get(pk=destino_pk)
    if origen.gris_disponible:
        nuevo_cambio = cambios(tipo='dorado',origen=orig,destino=des)
        nuevo_cambio.save()
        orig.gris_disponible = False
        orig.save()    
        des.dorado += 1
        des.save()
    return redirect('estado')