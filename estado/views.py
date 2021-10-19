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

def transaccion(request):
    context = {}
    context['nombreSeccion']='¿Estas seguro?'
    if request.method == "POST":
        form = CambioForm(request.POST)
        user = request.user
        if user.gris_disponible:
            cambio = form.save(commit=False)
            dest = cambio.destino
            if user != dest:
                context['form'] = form
                if cambio.tipo == 'Naranja':
                    if dest.equipo != user.equipo:
                        dest.naranja += 1
                    else:
                        context['catch'] = "Sombreros naranjas son para miembros de otro equipo"
                        return render(request, 'estado/cambiar.html',context)
                if cambio.tipo == 'Azul':
                    if dest.equipo == user.equipo:
                        dest.azul += 1
                    else:
                        context['catch'] = "Sombreros Azules son para miembros de tu equipo"
                        return render(request, 'estado/cambiar.html',context)
                cambio.origen = user
                tipo = cambio.tipo
                user.gris_disponible = False
                user.save()
                dest.save()
                cambio.save()
                return redirect('estado')
            else:
                context['catch'] = "Te autoseleccionaste, ¿eres tan bueno?"
    else:
        form = CambioForm()
    context['form'] = form
    return render(request, 'estado/cambiar.html',context)


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


