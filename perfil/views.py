from django import forms
from perfil.models import Usuario,Equipo
from estado.models import cambios
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from perfil.forms import SignInForm, LoginForm,MiInfo
from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string

UserModel = get_user_model()

def register_request(request):
    if request.method == 'GET':
        form = SignInForm()
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('login')
        else:
            form = SignInForm(request.POST)
    return render(request, 'perfil/registro.html',{'form': form})

class LogoutUsuario(LogoutView):
    success_url = 'home'

class LoginUsuario(LoginView):
    form_class = LoginForm
    template_name = 'perfil/signin.html'
    success_url = reverse_lazy('home')
    
    def get_context_data(self, **kwargs):
        context = super(LoginUsuario, self).get_context_data(**kwargs)
        context['title'] = 'Mi perfil'
        return context


class miPerfil(LoginRequiredMixin, DetailView):
    template_name = 'perfil/miPerfil.html'
    model = Usuario
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super(miPerfil, self).get_context_data(**kwargs)
        context['title'] = 'Mi perfil'
        context['nombreSeccion'] = 'Mi perfil'
        context['numEquipo'] = 'Sin asignar'
        user = Usuario.objects.filter(pk=self.request.user.id).first()
        context['transferencias'] = cambios.objects.filter(destino=user)
        context['perfil'] = user
        equipo = user.equipo
        if equipo is not None:
            context['nombreEquipo'] = equipo.name
            context['numeroEquipo'] = equipo.numero
            context['puntosEquipo'] = equipo.puntos
        else:
            context['nombreEquipo'] = 'Sin asignar'
        return context

    def get_queryset(self, *args, **kwargs):
        return Usuario.objects.filter(pk=self.request.user.id)

class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = MiInfo
    template_name = 'perfil/editar.html'
    login_url = 'login'
    success_url = reverse_lazy('perfil')

    def get_context_data(self, **kwargs):
        context = super(UsuarioUpdateView, self).get_context_data(**kwargs)
        context['nombreSeccion']='Edita tu perfil'
