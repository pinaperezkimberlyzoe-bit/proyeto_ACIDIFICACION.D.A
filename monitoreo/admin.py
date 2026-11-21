from django.contrib import admin
from .models import RegistroAcidificacion

@admin.register(RegistroAcidificacion)
class RegistroAcidificacionAdmin(admin.ModelAdmin):
    list_display = ('nombre_equipo', 'fecha_hora', 'ph_1', 'ph_2', 'ph_3', 'ph_4')