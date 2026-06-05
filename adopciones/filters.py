import django_filters

from adopciones.models import Fundacion


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