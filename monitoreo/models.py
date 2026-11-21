from django.db import models
from django.db import models
from django.contrib.auth.models import User

class RegistroAcidificacion(models.Model):
    nombre_equipo = models.CharField(max_length=100)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    
    # Deben llamarse exactamente así:
    ph_1 = models.DecimalField(max_digits=4, decimal_places=2)
    ph_2 = models.DecimalField(max_digits=4, decimal_places=2)
    ph_3 = models.DecimalField(max_digits=4, decimal_places=2)
    ph_4 = models.DecimalField(max_digits=4, decimal_places=2)
    
    co2_1 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    co2_2 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    co2_3 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    co2_4 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    
    leyenda = models.TextField(blank=True, null=True)
    leyenda = models.TextField(verbose_name="Leyenda / Interpretación", blank=True, null=True)

    def __str__(self):
        return f"Equipo: {self.equipo} - {self.fecha_registro.strftime('%Y-%m-%d %H:%M')}"