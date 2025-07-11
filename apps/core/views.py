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
from .models import SiteConfiguration, SocialNetwork, MenuItem

class HomeView(TemplateView):
    template_name = 'core-inicio.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
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
