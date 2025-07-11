from django.shortcuts import render, get_object_or_404
from django.db.models import Sum
from django.http import JsonResponse
from .models import (
    EstadisticasImpacto, EstadisticaPorEstado, MetricasImpacto,
    TestimonioEgresado, InformeAnual, Aliado, ConfiguracionAliados,
    CarouselImage
)

def testimonio_impacto(request):
    """Vista principal para la página de testimonio e impacto"""
    # Obtener o crear instancias singleton
    estadisticas_impacto, created = EstadisticasImpacto.objects.get_or_create(
        pk=1,
        defaults={
            'titulo': 'Nuestro Impacto en México',
            'subtitulo': 'Conoce el alcance de nuestro programa educativo a nivel nacional'
        }
    )
    
    metricas_impacto, created = MetricasImpacto.objects.get_or_create(pk=1)
    
    configuracion_aliados, created = ConfiguracionAliados.objects.get_or_create(
        pk=1,
        defaults={'titulo': 'Nuestros Aliados'}
    )
    
    # Obtener datos para el contexto
    context = {
        # Sección de estadísticas
        'estadisticas_impacto': estadisticas_impacto,
        'estadisticas_por_estado': EstadisticaPorEstado.objects.all(),
        
        # Sección de métricas
        'metricas_impacto': metricas_impacto,
        
        # Sección de testimonio
        'testimonio_egresado': TestimonioEgresado.objects.filter(activo=True).first(),
        
        # Sección de carrusel de imágenes
        'carousel_images': CarouselImage.objects.filter(is_active=True).order_by('order'),
        
        # Sección de informe anual
        'informe_anual': InformeAnual.objects.filter(activo=True).first(),
        
        # Sección de aliados
        'configuracion_aliados': configuracion_aliados,
        'aliados': Aliado.objects.filter(activo=True),
        
        # Datos adicionales para el frontend
        'total_egresados_nacional': EstadisticaPorEstado.objects.aggregate(
            total=Sum('total_egresados')
        )['total'] or 0,
    }
    
    return render(request, 'impact.html', context)

def api_estadisticas_mapa(request):
    """API endpoint para obtener datos del mapa en formato JSON"""
    
    estadisticas = EstadisticaPorEstado.objects.all()
    
    data = {
        'estados': []
    }
    
    for estadistica in estadisticas:
        data['estados'].append({
            'codigo': estadistica.estado,
            'nombre': estadistica.get_estado_display(),
            'total_egresados': estadistica.total_egresados,
            'egresados_hombres': estadistica.egresados_hombres,
            'egresados_mujeres': estadistica.egresados_mujeres,
            'porcentaje_hombres': estadistica.porcentaje_hombres,
            'porcentaje_mujeres': estadistica.porcentaje_mujeres,
        })
    
    return JsonResponse(data)

def api_metricas_impacto(request):
    """API endpoint para obtener métricas de impacto en formato JSON"""
    
    try:
        metricas = MetricasImpacto.objects.first()
        
        if not metricas:
            return JsonResponse({'error': 'No hay métricas disponibles'}, status=404)
        
        data = {
            'metricas': [
                {
                    'label': 'Incrementó sus ingresos',
                    'porcentaje': metricas.incremento_ingresos,
                },
                {
                    'label': 'Recibió un ascenso',
                    'porcentaje': metricas.recibio_ascenso,
                },
                {
                    'label': 'Emprendió un negocio',
                    'porcentaje': metricas.emprendi_negocio,
                },
                {
                    'label': 'Continuó estudios superiores',
                    'porcentaje': metricas.continuo_estudios,
                },
                {
                    'label': 'Formación continua',
                    'porcentaje': metricas.formacion_continua,
                }
            ]
        }
        
        return JsonResponse(data)
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def api_carousel_images(request):
    """API endpoint para obtener imágenes del carrusel en formato JSON"""
    
    try:
        images = CarouselImage.objects.filter(is_active=True).order_by('order')
        
        data = {
            'images': [
                {
                    'title': image.title,
                    'image_url': image.image.url,
                    'order': image.order,
                }
                for image in images
            ]
        }
        
        return JsonResponse(data)
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)