from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from perfil.models import Usuario,Equipo
from estado.models import cambios
from django.views.generic import ListView, DetailView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from estado.forms import CambioForm
from django.urls import reverse_lazy

class transaccion(CreateView):
    model = cambios
    form_class = CambioForm
    template_name = 'estado/cambiar.html'
    success_url = reverse_lazy('estado')
    usuario = ''

    def get_context_data(self, **kwargs):
        context = super(transaccion, self).get_context_data(**kwargs)
        context['nombreSeccion'] = '¿Estas seguro?'
        return context


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


