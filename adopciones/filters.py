import django_filters

from adopciones.models import (
    Fundacion,
    Mascota,
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