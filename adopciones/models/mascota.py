from django.db import models

from .fundacion import Fundacion


class Mascota(models.Model):

    ESPECIES = [
        ("Perro", "Perro"),
        ("Gato", "Gato"),
    ]

    SEXOS = [
        ("Macho", "Macho"),
        ("Hembra", "Hembra"),
    ]

    ESTADOS = [
        ("Disponible", "Disponible"),
        ("Adoptado", "Adoptado"),
    ]

    nombre = models.CharField(max_length=100)

    especie = models.CharField(
        max_length=20,
        choices=ESPECIES
    )

    raza = models.CharField(max_length=100)

    edad = models.PositiveIntegerField()

    sexo = models.CharField(
        max_length=20,
        choices=SEXOS
    )

    descripcion = models.TextField()

    foto = models.URLField(
        blank=True,
        default=""
    )

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default="Disponible"
    )

    fundacion = models.ForeignKey(
        Fundacion,
        on_delete=models.CASCADE,
        related_name="mascotas"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre