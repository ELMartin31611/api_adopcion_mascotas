from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)

from adopciones.models import Mascota

from adopciones.serializers import (
    MascotaSerializer,
)

from adopciones.permissions import (
    IsStaffOrReadOnly,
)

from adopciones.filters import (
    MascotaFilter,
)

from adopciones.pagination import (
    StandardPagination,
)


class MascotaViewSet(viewsets.ModelViewSet):

    queryset = Mascota.objects.select_related(
        "fundacion"
    )

    serializer_class = MascotaSerializer

    permission_classes = [
        IsStaffOrReadOnly
    ]

    pagination_class = StandardPagination

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_class = MascotaFilter

    search_fields = [
        "nombre",
        "raza",
        "descripcion",
    ]

    ordering_fields = [
        "nombre",
        "edad",
        "created_at",
    ]

    ordering = [
        "nombre"
    ]