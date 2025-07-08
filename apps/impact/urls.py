from django.urls import path
from . import views

app_name = 'testimonio'

urlpatterns = [
    # Página principal
    path('', views.testimonio_impacto, name='testimonio_impacto'),
    
    # API endpoints para datos dinámicos
    path('api/estadisticas-mapa/', views.api_estadisticas_mapa, name='api_estadisticas_mapa'),
    path('api/metricas-impacto/', views.api_metricas_impacto, name='api_metricas_impacto'),
]