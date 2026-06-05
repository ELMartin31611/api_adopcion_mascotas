from django.db import models
from django.contrib.auth.models import User

from .mascota import Mascota


class SolicitudAdopcion(models.Model):

    ESTADO_CHOICES = [
        ("Pendiente", "Pendiente"),
        ("Aprobada", "Aprobada"),
        ("Rechazada", "Rechazada"),
    ]

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="solicitudes"
    )

    mascota = models.ForeignKey(
        Mascota,
        on_delete=models.CASCADE,
        related_name="solicitudes"
    )

    fecha = models.DateTimeField(
        auto_now_add=True
    )

    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default="Pendiente"
    )

    class Meta:
        ordering = ["-fecha"]

    def __str__(self):
        return f"{self.usuario} → {self.mascota} ({self.estado})"