from django.db import models
from django.contrib.auth.models import User

from .fundacion import Fundacion


class Donacion(models.Model):

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="donaciones"
    )

    fundacion = models.ForeignKey(
        Fundacion,
        on_delete=models.CASCADE,
        related_name="donaciones"
    )

    monto = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    fecha = models.DateTimeField(
        auto_now_add=True
    )

    metodo_pago = models.CharField(
        max_length=50
    )

    class Meta:
        ordering = ["-fecha"]

    def __str__(self):
        return f"{self.usuario} → {self.monto}"