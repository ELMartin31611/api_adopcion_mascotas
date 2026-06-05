from rest_framework import serializers
from adopciones.models import Rescate


class RescateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rescate
        fields = "__all__"