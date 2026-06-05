from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from adopciones.models import Donacion
from adopciones.serializers import DonacionSerializer
from adopciones.pagination import StandardPagination
from adopciones.filters import DonacionFilter


class DonacionViewSet(viewsets.ModelViewSet):

    queryset = Donacion.objects.all()
    serializer_class = DonacionSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_class = DonacionFilter

    search_fields = ["metodo_pago"]

    ordering_fields = ["fecha", "monto"]

    def perform_create(self, serializer):
        serializer.save(
            usuario=self.request.user
        )