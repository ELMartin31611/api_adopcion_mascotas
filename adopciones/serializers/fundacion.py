from rest_framework import serializers

from adopciones.models import Fundacion


class FundacionSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = Fundacion

        fields = [
            "id",
            "nombre",
            "descripcion",
            "direccion",
            "telefono",
            "correo",
            "is_active",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
        ]