from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from adopciones.models import Rescate
from adopciones.serializers import RescateSerializer
from adopciones.pagination import StandardPagination
from adopciones.filters import RescateFilter


class RescateViewSet(viewsets.ModelViewSet):

    queryset = Rescate.objects.all()
    serializer_class = RescateSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_class = RescateFilter

    search_fields = ["lugar_encontrado"]

    ordering_fields = ["fecha_rescate"]