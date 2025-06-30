from django.urls import path
from . import views

app_name = 'proyectos'

urlpatterns = [
    # Página principal de proyectos
    path('', views.ProyectosView.as_view(), name='proyectos'),
    
    # Vista alternativa con función (comentada por defecto)
    # path('', views.proyectos_view, name='index'),
    
    # Vista para mostrar PDFs de convocatorias
path('convocatoria/<int:documento_id>/', views.ver_documento_convocatoria, name='ver_documento_convocatoria'),
]