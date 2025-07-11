from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Q
from .models import (
    QuienesSomosConfig, Mision, Vision, Valor, ImagenCollage,
    MiembroEquipo, ObjetivoDesarrolloSostenible, SeccionProgramasODS
)


class QuienesSomosView(TemplateView):
    """
    Vista principal para la página Quiénes Somos
    """
    template_name = 'quienes_somos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Configuración principal
        context['config'] = QuienesSomosConfig.objects.filter(activo=True).first()
        
        # Misión
        context['mision'] = Mision.objects.filter(activo=True).first()
        
        # Visión
        context['vision'] = Vision.objects.filter(activo=True).first()
        
        # Valores
        context['valores'] = Valor.objects.filter(activo=True).order_by('orden', 'nombre')
        
        # Imágenes para collages
        context['imagenes_mision'] = ImagenCollage.objects.filter(
            seccion='mision', 
            activo=True
        ).order_by('orden')[:3]  # Máximo 3 imágenes para el collage
        
        context['imagenes_vision_valores'] = ImagenCollage.objects.filter(
            seccion='vision_valores', 
            activo=True
        ).order_by('orden')[:4]  # Máximo 4 imágenes para el collage
        
        # Miembros del equipo
        context['miembros_equipo'] = MiembroEquipo.objects.filter(activo=True).order_by('orden', 'nombre')
        
        # Objetivos de Desarrollo Sostenible
        context['objetivos_ods'] = ObjetivoDesarrolloSostenible.objects.filter(activo=True).order_by('orden', 'numero')
        
        # Configuración de la sección ODS
        context['config_ods'] = SeccionProgramasODS.objects.filter(activo=True).first()
        
        return context


def get_quienes_somos_data():
    """
    Función helper para obtener todos los datos de Quiénes Somos
    Útil para incluir en otras vistas como context processors
    """
    data = {
        'config': QuienesSomosConfig.objects.filter(activo=True).first(),
        'mision': Mision.objects.filter(activo=True).first(),
        'vision': Vision.objects.filter(activo=True).first(),
        'valores': Valor.objects.filter(activo=True).order_by('orden', 'nombre'),
        'imagenes_mision': ImagenCollage.objects.filter(
            seccion='mision', 
            activo=True
        ).order_by('orden')[:3],
        'imagenes_vision_valores': ImagenCollage.objects.filter(
            seccion='vision_valores', 
            activo=True
        ).order_by('orden')[:4],
        'miembros_equipo': MiembroEquipo.objects.filter(activo=True).order_by('orden', 'nombre'),
        'objetivos_ods': ObjetivoDesarrolloSostenible.objects.filter(activo=True).order_by('orden', 'numero'),
        'config_ods': SeccionProgramasODS.objects.filter(activo=True).first(),
    }
    return data
