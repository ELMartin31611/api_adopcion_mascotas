from django.urls import include, path

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

from adopciones.views.health import health_check

from adopciones.views.auth import (
    RegisterView,
    LogoutView,
)

from adopciones.views.fundacion import (
    FundacionViewSet,
)

from adopciones.views.mascota import (
    MascotaViewSet,
)

from adopciones.views.solicitud import (
    SolicitudAdopcionViewSet,
)

from adopciones.views.rescate import RescateViewSet
from adopciones.views.donacion import DonacionViewSet


from adopciones.serializers.auth import (
    CustomTokenView,
)

router = DefaultRouter()

router.register(
    "fundaciones",
    FundacionViewSet,
    basename="fundacion"
)

router.register(
    "mascotas",
    MascotaViewSet,
    basename="mascota"
)

router.register(
    "solicitudes",
    SolicitudAdopcionViewSet,
    basename="solicitud"
)

router.register("rescates", RescateViewSet, basename="rescate")
router.register("donaciones", DonacionViewSet, basename="donacion")

urlpatterns = [
    path("health/", health_check),

    path(
        "auth/register/",
        RegisterView.as_view()
    ),

    path(
        "auth/login/",
        CustomTokenView.as_view()
    ),

    path(
        "auth/token/refresh/",
        TokenRefreshView.as_view()
    ),

    path(
        "auth/token/verify/",
        TokenVerifyView.as_view()
    ),

    path(
        "auth/logout/",
        LogoutView.as_view()
    ),

    path(
        "",
        include(router.urls)
    ),
]



