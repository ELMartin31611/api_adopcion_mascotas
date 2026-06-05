from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from adopciones.models import SolicitudAdopcion
from adopciones.serializers import SolicitudAdopcionSerializer
from adopciones.pagination import StandardPagination
from adopciones.filters import SolicitudFilter


class SolicitudAdopcionViewSet(viewsets.ModelViewSet):

    queryset = SolicitudAdopcion.objects.all()
    serializer_class = SolicitudAdopcionSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_class = SolicitudFilter

    search_fields = [
        "mascota__nombre",
    ]

    ordering_fields = [
        "fecha",
        "estado",
    ]

    ordering = ["-fecha"]

    def perform_create(self, serializer):
        serializer.save(
            usuario=self.request.user
        )