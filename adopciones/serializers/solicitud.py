from rest_framework import serializers

from adopciones.models import SolicitudAdopcion


class SolicitudAdopcionSerializer(serializers.ModelSerializer):

    usuario = serializers.ReadOnlyField(
        source="usuario.username"
    )

    class Meta:
        model = SolicitudAdopcion

        fields = [
            "id",
            "usuario",
            "mascota",
            "fecha",
            "estado",
        ]

        read_only_fields = [
            "id",
            "fecha",
            "usuario",
        ]