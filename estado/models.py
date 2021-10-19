from django.db import models
from perfil.models import Usuario

class cambios(models.Model):
    TIPOS = [
        ('Naranja','naranja'),
        ('Azul','azul')
    ]
    tipo = models.CharField(
        max_length=10,
        choices = TIPOS,
    )
    origen = models.ForeignKey(
        Usuario,
        default=None,
        on_delete=models.CASCADE,
        related_name="origen_id"
    )
    destino = models.ForeignKey(
        Usuario,
        default=None,
        on_delete=models.CASCADE,
        related_name="destino_id"
    )


