from django.contrib import admin
from .models import Mascota, Fundacion, Rescate, SolicitudAdopcion


# =========================
# MASCOTA
# =========================
@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "edad")
    search_fields = ("nombre",)


# =========================
# FUNDACION
# =========================
@admin.register(Fundacion)
class FundacionAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)


# =========================
# RESCATE
# =========================
@admin.register(Rescate)
class RescateAdmin(admin.ModelAdmin):
    list_display = ("id", "mascota")
    search_fields = ("mascota__nombre",)


# =========================
# SOLICITUD DE ADOPCION
# =========================
@admin.register(SolicitudAdopcion)
class SolicitudAdopcionAdmin(admin.ModelAdmin):
    list_display = ("id", "usuario", "mascota", "estado", "fecha")
    list_filter = ("estado",)
    search_fields = ("usuario__username", "mascota__nombre")