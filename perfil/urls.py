from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginUsuario.as_view(), name='login'),
    path('logout/', views.LogoutUsuario.as_view(), name="logout"),
    path('registro/', views.register_request, name="registro"),
    path('mi_perfil<int:pk>/', views.miPerfil.as_view(),name='perfil'),
    path('editar<int:pk>/',views.UsuarioUpdateView.as_view(),name='editar')
]