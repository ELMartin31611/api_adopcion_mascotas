from django.db import models


class Fundacion(models.Model):

    nombre = models.CharField(max_length=150,unique=True)
    descripcion = models.TextField(blank=True, default="")
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Fundacion"
        verbose_name_plural = "Fundaciones"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre