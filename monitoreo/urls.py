from django.urls import path
from .views import (
    RegistroListView,
    RegistroCreateView,
    RegistroUpdateView,
    RegistroDetailView,
    RegistroDeleteView,
)

urlpatterns = [
    path('', RegistroListView.as_view(), name='lista_registros'),
    path('nuevo/', RegistroCreateView.as_view(), name='crear_registro'),
    path('detalle/<int:pk>/', RegistroDetailView.as_view(), name='detalle_registro'),
    path('editar/<int:pk>/', RegistroUpdateView.as_view(), name='editar_registro'),
    path('eliminar/<int:pk>/', RegistroDeleteView.as_view(), name='eliminar_registro'),
]