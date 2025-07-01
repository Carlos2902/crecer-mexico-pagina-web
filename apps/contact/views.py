# views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from apps.core.models import SiteConfiguration, MenuItem, SocialNetwork
# Importa otros modelos que necesites según tu aplicación

def contact_view(request):
    """
    Vista para la página de contacto con todos los datos necesarios para base.html
    """
    
    # Obtener configuración del sitio
    site_config = SiteConfiguration.objects.first()
    
    # Obtener menú de navegación
    header_menu = MenuItem.objects.filter(
        is_active=True,
        location='header'  # Ajusta según tu modelo
    ).order_by('order')
    
    # Obtener redes sociales
    social_networks = SocialNetwork.objects.filter(is_active=True).order_by('order')
    
    # Obtener menú del footer (si tienes)
    footer_menu = MenuItem.objects.filter(
        is_active=True,
        location='footer'  # Ajusta según tu modelo
    ).order_by('order')
    
    # Obtener datos específicos de la página de contacto (si tienes)
  #  try:
  #      hero = HeroSection.objects.get(page='contact')  # Ajusta según tu modelo
 #   except HeroSection.DoesNotExist:
 #       hero = None
    
    # Preparar contexto base
    context = {
        # Variables requeridas por base.html
        'site_config': site_config,
        'header_menu': header_menu,
        'social_networks': social_networks,
        'footer_menu': footer_menu,
        
        # Variables específicas de contacto
      #  'hero': hero,
        'page_title': 'Contacto',
    }
    
    # Procesar formulario si es POST
    if request.method == 'POST':
        # Obtener datos del formulario
        nombre = request.POST.get('nombre', '').strip()
        correo = request.POST.get('correo', '').strip()
        telefono = request.POST.get('telefono', '').strip()
        asunto = request.POST.get('asunto', '').strip()
        mensaje = request.POST.get('mensaje', '').strip()
        
        # Validación básica
        if not all([nombre, correo, telefono, mensaje]):
            messages.error(request, 'Todos los campos marcados son obligatorios.')
            return render(request, 'contact.html', context)
        
        try:
            # Enviar email (configura tu email backend en settings.py)
            email_subject = f"Nuevo mensaje de contacto: {asunto or 'Sin asunto'}"
            email_message = f"""
            Nuevo mensaje de contacto recibido:
            
            Nombre: {nombre}
            Correo: {correo}
            Teléfono: {telefono}
            Asunto: {asunto}
            
            Mensaje:
            {mensaje}
            """
            
            send_mail(
                email_subject,
                email_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],  # Define esto en settings.py
                fail_silently=False,
            )
            
            messages.success(request, '¡Mensaje enviado exitosamente! Nos pondremos en contacto contigo pronto.')
            
            # Si es una petición AJAX, devolver JSON
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Mensaje enviado exitosamente!'})
                
        except Exception as e:
            messages.error(request, 'Hubo un error al enviar el mensaje. Por favor, inténtalo de nuevo.')
            
            # Si es una petición AJAX, devolver error
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'message': 'Error al enviar el mensaje.'})
    
    return render(request, 'contact.html', context)


# ALTERNATIVA: Crear un context processor para variables globales
# context_processors.py
def global_context(request):
    """
    Context processor para variables que se necesitan en todas las páginas
    """
    return {
        'site_config': SiteConfiguration.objects.first(),
        'header_menu': MenuItem.objects.filter(is_active=True, location='header').order_by('order'),
        'social_networks': SocialNetwork.objects.filter(is_active=True).order_by('order'),
        'footer_menu': MenuItem.objects.filter(is_active=True, location='footer').order_by('order'),
    }

# Si usas el context processor, tu vista puede ser más simple:
def contact_view_simple(request):
    """
    Vista simplificada usando context processor
    """
    context = {
    #    'hero': HeroSection.objects.filter(page='contact').first(),
        'page_title': 'Contacto',
    }
    
    if request.method == 'POST':
        # Lógica del formulario aquí
        pass
    
    return render(request, 'contact.html', context)

