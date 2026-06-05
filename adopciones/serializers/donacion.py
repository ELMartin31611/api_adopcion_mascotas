from rest_framework import serializers
from adopciones.models import Donacion


class DonacionSerializer(serializers.ModelSerializer):

    usuario = serializers.ReadOnlyField(
        source="usuario.username"
    )

    class Meta:
        model = Donacion

        fields = [
            "id",
            "usuario",
            "fundacion",
            "monto",
            "fecha",
            "metodo_pago",
        ]

        read_only_fields = [
            "id",
            "usuario",
            "fecha",
        ]