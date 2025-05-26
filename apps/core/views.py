from django.views.generic import TemplateView
from django.shortcuts import render

from .models import (
    SiteConfiguration,
    SocialNetwork,
    MenuItem,
    Hero,
    Program,
    Testimonial,
    FeaturedVideo,
    HomepageSection
)


def get_common_context():
    """
    Obtiene el contexto común para todas las páginas
    """
    try:
        config = SiteConfiguration.objects.first()
    except SiteConfiguration.DoesNotExist:
        config = None
    
    context = {
        'site_config': config,
        'social_networks': SocialNetwork.objects.filter(is_active=True).order_by('order'),
        'header_menu': MenuItem.objects.filter(
            is_active=True, 
            parent__isnull=True, 
            location__in=['header', 'both']
        ).order_by('order'),
        'footer_menu': MenuItem.objects.filter(
            is_active=True, 
            parent__isnull=True, 
            location__in=['footer', 'both']
        ).order_by('order'),
    }
    
    return context


class HomeView(TemplateView):
    template_name = 'core-inicio.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Añadir contexto común
        context.update(get_common_context())
        
        # Obtener las secciones activas y su orden
        sections = HomepageSection.objects.filter(is_active=True).order_by('order')
        context['sections'] = sections
        
        # Añadir datos para cada sección
        if sections.filter(section='hero').exists():
            context['hero'] = Hero.objects.filter(is_active=True).first()
        
        if sections.filter(section='programs').exists():
            context['programs'] = Program.objects.filter(is_active=True).order_by('order')
            context['programs_section'] = sections.get(section='programs')
        
        if sections.filter(section='testimonial').exists():
            # Obtener el testimonio destacado, o el primero si no hay destacado
            testimonial = Testimonial.objects.filter(is_active=True, is_featured=True).first()
            if not testimonial:
                testimonial = Testimonial.objects.filter(is_active=True).first()
            context['testimonial'] = testimonial
            context['testimonial_section'] = sections.get(section='testimonial')
        
        if sections.filter(section='video').exists():
            context['featured_video'] = FeaturedVideo.objects.filter(is_active=True).first()
            context['video_section'] = sections.get(section='video')
        
        return context
