from rest_framework import serializers

from adopciones.models import Mascota


class MascotaSerializer(serializers.ModelSerializer):

    fundacion_nombre = serializers.CharField(
        source="fundacion.nombre",
        read_only=True
    )

    class Meta:
        model = Mascota

        fields = [
            "id",
            "nombre",
            "especie",
            "raza",
            "edad",
            "sexo",
            "descripcion",
            "foto",
            "estado",
            "fundacion",
            "fundacion_nombre",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
        ]