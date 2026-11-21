import io
import urllib, base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import RegistroAcidificacion
from .forms import RegistroForm

def calcular_co2(ph):
    """Aplica la fórmula matemática para convertir pH en concentración de CO2 (μatm)."""
    return round(630 + (8 - ph) * 1000, 2)

class RegistroListView(ListView):
    model = RegistroAcidificacion
    template_name = 'monitoreo/lista.html'
    context_object_name = 'registros'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(nombre_equipo__icontains=query)
        return queryset

class RegistroDetailView(DetailView):
    model = RegistroAcidificacion
    template_name = 'monitoreo/detalle.html'
    context_object_name = 'registro'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        registro = self.object
        
        # 1. Obtener los valores de pH y calcular su respectivo CO2 para la tabla
        phs = [registro.ph_1, registro.ph_2, registro.ph_3, registro.ph_4]
        co2_calculados = [calcular_co2(ph) for ph in phs]
        
        # Empaquetamos los datos para que la tabla los lea perfectamente
        context['tomas_datos'] = zip(['Toma 1', 'Toma 2', 'Toma 3', 'Toma 4'], phs, co2_calculados)

        # 2. Generación de gráfica con Matplotlib renderizada en Base64
        tomas = ['Toma 1', 'Toma 2', 'Toma 3', 'Toma 4']
        
        plt.figure(figsize=(6, 3.5))
        plt.plot(tomas, phs, marker='o', color='#2563eb', linewidth=2.5, markersize=8)
        plt.title('Variación de pH por Toma de Muestra', fontsize=12, fontweight='bold', color='#333')
        plt.xlabel('Momentos de Medición', fontsize=10)
        plt.ylabel('Nivel de pH', fontsize=10)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.ylim(0, 14)

        # Guardar gráfica en búfer de memoria
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png', bbox_inches='tight')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        plt.close()
        
        context['grafica'] = base64.b64encode(image_png).decode('utf-8')
        return context

class RegistroCreateView(SuccessMessageMixin, CreateView):
    model = RegistroAcidificacion
    form_class = RegistroForm
    template_name = 'monitoreo/form.html'
    success_url = reverse_lazy('lista_registros')
    success_message = "¡Registro de laboratorio creado exitosamente!"

class RegistroUpdateView(SuccessMessageMixin, UpdateView):
    model = RegistroAcidificacion
    form_class = RegistroForm
    template_name = 'monitoreo/form.html'
    success_url = reverse_lazy('lista_registros')
    success_message = "¡Registro actualizado correctamente!"

class RegistroDeleteView(SuccessMessageMixin, DeleteView):
    model = RegistroAcidificacion
    template_name = 'monitoreo/confirmar_eliminar.html'
    success_url = reverse_lazy('lista_registros')
    success_message = "¡Registro eliminado correctamente!"