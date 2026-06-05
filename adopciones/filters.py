import django_filters

from adopciones.models import (
    Fundacion,
    Mascota,
    SolicitudAdopcion,
    Rescate, 
    Donacion
)


class FundacionFilter(
    django_filters.FilterSet
):

    nombre = django_filters.CharFilter(
        lookup_expr="icontains"
    )

    class Meta:
        model = Fundacion

        fields = [
            "is_active",
        ]


class MascotaFilter(
    django_filters.FilterSet
):

    class Meta:
        model = Mascota

        fields = [
            "especie",
            "sexo",
            "estado",
            "fundacion",
        ]

class SolicitudFilter(
    django_filters.FilterSet
):

    class Meta:
        model = SolicitudAdopcion

        fields = [
            "estado",
            "mascota",
        ]


class RescateFilter(django_filters.FilterSet):

    class Meta:
        model = Rescate
        fields = ["fecha_rescate"]


class DonacionFilter(django_filters.FilterSet):

    class Meta:
        model = Donacion
        fields = ["fundacion", "metodo_pago"]