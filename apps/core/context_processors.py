from .models import SiteConfiguration, SocialNetwork, MenuItem

def core_context(request):
    """
    Context processor para datos del header/footer que estarán disponibles
    en todas las templates que usen este context processor
    """
    try:
        config = SiteConfiguration.objects.first()
    except SiteConfiguration.DoesNotExist:
        config = None
    
    try:
        social_networks = SocialNetwork.objects.filter(is_active=True).order_by('order')
    except:
        social_networks = []
    
    try:
        header_menu = MenuItem.objects.filter(
            is_active=True, 
            parent__isnull=True, 
            location__in=['header', 'both']
        ).order_by('order')
    except:
        header_menu = []
    
    try:
        footer_menu = MenuItem.objects.filter(
            is_active=True, 
            parent__isnull=True, 
            location__in=['footer', 'both']
        ).order_by('order')
    except:
        footer_menu = []
    
    context = {
        'site_config': config,
        'social_networks': social_networks,
        'header_menu': header_menu,
        'footer_menu': footer_menu,
    }
    
    return context