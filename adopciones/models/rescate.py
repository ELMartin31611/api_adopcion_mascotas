from django.db import models

from .mascota import Mascota


class Rescate(models.Model):

    mascota = models.OneToOneField(
        Mascota,
        on_delete=models.CASCADE,
        related_name="rescate"
    )

    lugar_encontrado = models.CharField(
        max_length=255
    )

    fecha_rescate = models.DateField()

    estado_salud = models.CharField(
        max_length=100
    )

    descripcion = models.TextField()

    class Meta:
        ordering = ["-fecha_rescate"]

    def __str__(self):
        return f"{self.mascota} - {self.lugar_encontrado}"