from django.db.models import Count

from django_filters.rest_framework import (
    DjangoFilterBackend
)

from rest_framework import viewsets

from rest_framework.decorators import (
    action
)

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)

from rest_framework.response import (
    Response
)

from adopciones.models import (
    Fundacion
)

from adopciones.serializers.fundacion import (
    FundacionSerializer
)

from adopciones.filters import (
    FundacionFilter
)

from adopciones.pagination import (
    StandardPagination
)

from adopciones.permissions import (
    IsStaffOrReadOnly
)


class FundacionViewSet(
    viewsets.ModelViewSet
):

    queryset = Fundacion.objects.all()

    serializer_class = (
        FundacionSerializer
    )

    permission_classes = [
        IsStaffOrReadOnly
    ]

    pagination_class = (
        StandardPagination
    )

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_class = (
        FundacionFilter
    )

    search_fields = [
        "nombre",
        "descripcion",
        "direccion",
    ]

    ordering_fields = [
        "nombre",
        "created_at",
    ]

    ordering = [
        "nombre"
    ]

    @action(
        detail=False,
        methods=["get"],
        url_path="stats"
    )
    def stats(self, request):

        qs = Fundacion.objects.annotate(
            num_mascotas=Count(
                "mascotas",
                distinct=True
            )
        )

        return Response(
            {
                "total": qs.count(),
                "activas": qs.filter(
                    is_active=True
                ).count(),
                "inactivas": qs.filter(
                    is_active=False
                ).count(),
            }
        )