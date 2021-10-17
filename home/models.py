from django.db import models

class Unidad(models.Model):
    unidad = models.CharField(
        max_length=50,
        unique=True,
    )
    actual = models.BooleanField(
        blank=False,
        default=False,
    )

    def __str__(self):
        return self.unidad


class Tema(models.Model):
    nombre = models.CharField(
        max_length=200,
        unique=True,
    )
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre