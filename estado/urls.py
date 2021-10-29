from django.conf.urls import url
from django.urls import path
from estado.views import estado,transaccion,cambiosList


urlpatterns = [
    path('ver_cambio/<int:pk>/',cambiosList.as_view(),name='cambios'),
    path('crear_cambio/', transaccion, name='cambiar'),
    path('', estado.as_view(), name='estado'),
]
