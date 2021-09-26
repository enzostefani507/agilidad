from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url('', views.estado.as_view(), name='estado'),
    url('transferir_azul/<int:origen_pk>/<int:destino_pk>/', views.transferir_azul,name='transferir_azul'),
    url('transferir_dorado/<int:origen_pk>/<int:destino_pk>/', views.transferir_dorado,name='transferir_dorado')
]
