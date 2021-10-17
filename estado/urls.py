from django.conf.urls import url
from estado.views import estado,transaccion


urlpatterns = [
    url('crear_cambio/', transaccion, name='cambiar'),
    url('', estado.as_view(), name='estado'),
]
