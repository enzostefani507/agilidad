from django.db import models
from perfil.models import Usuario

class cambios(models.Model):
    tipo = models.CharField(
        max_length=50
    )
    origen = models.ForeignKey(
        Usuario,
        default=None,
        on_delete=models.CASCADE,
        related_name="cambio_origen"
    )
    destino = models.ForeignKey(
        Usuario,
        default=None,
        on_delete=models.CASCADE,
        related_name="cambio_destino"
    )