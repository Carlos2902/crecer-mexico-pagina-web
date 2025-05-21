from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


class TimeStampedModel(models.Model):
    """
    Modelo abstracto que incluye campos de seguimiento de creación y modificación
    """
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Fecha de creación"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Última actualización"))

    class Meta:
        abstract = True


class SocialNetwork(TimeStampedModel):
    """
    Modelo para las redes sociales de la organización
    """
    NETWORK_CHOICES = (
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('twitter', 'Twitter'),
        ('linkedin', 'LinkedIn'),
        ('youtube', 'YouTube'),
        ('tiktok', 'TikTok'),
        ('other', 'Otra'),
    )
    
    name = models.CharField(max_length=50, choices=NETWORK_CHOICES, verbose_name=_("Red social"))
    url = models.URLField(max_length=255, verbose_name=_("Enlace"))
    icon = models.CharField(max_length=50, blank=True, help_text=_("Clase de icono (ej: 'fab fa-facebook')"), verbose_name=_("Icono"))
    order = models.PositiveIntegerField(default=0, verbose_name=_("Orden"))
    is_active = models.BooleanField(default=True, verbose_name=_("Activo"))
    
    class Meta:
        verbose_name = _("Red social")
        verbose_name_plural = _("Redes sociales")
        ordering = ["order"]
    
    def __str__(self):
        return self.get_name_display()


class SiteConfiguration(TimeStampedModel):
    """
    Configuración global del sitio
    """
    site_name = models.CharField(max_length=100, default="Crecer México", verbose_name=_("Nombre del sitio"))
    logo = models.ImageField(upload_to='site/logo/', verbose_name=_("Logo principal"))
    logo_alt = models.ImageField(upload_to='site/logo/', blank=True, null=True, verbose_name=_("Logo alternativo"))
    favicon = models.ImageField(upload_to='site/favicon/', blank=True, null=True, verbose_name=_("Favicon"))
    
    # Información de contacto
    email = models.EmailField(verbose_name=_("Email principal"))
    phone = models.CharField(max_length=50, blank=True, verbose_name=_("Teléfono"))
    address = models.TextField(blank=True, verbose_name=_("Dirección"))
    
    # Textos del footer
    footer_text = models.TextField(blank=True, verbose_name=_("Texto del pie de página"))
    copyright_text = models.CharField(max_length=255, blank=True, verbose_name=_("Texto de copyright"))
    
    # Metadatos SEO
    meta_description = models.TextField(blank=True, verbose_name=_("Meta descripción"))
    meta_keywords = models.CharField(max_length=255, blank=True, verbose_name=_("Meta keywords"))
    
    # Google Analytics
    google_analytics_id = models.CharField(max_length=50, blank=True, verbose_name=_("ID de Google Analytics"))
    
    class Meta:
        verbose_name = _("Configuración del sitio")
        verbose_name_plural = _("Configuraciones del sitio")
    
    def __str__(self):
        return self.site_name
    
    def save(self, *args, **kwargs):
        # Solo permitir una instancia de configuración
        if SiteConfiguration.objects.exists() and not self.pk:
            raise ValidationError("Ya existe una configuración del sitio")
        return super().save(*args, **kwargs)


class MenuItem(TimeStampedModel):
    """
    Elementos para el menú de navegación
    """
    MENU_LOCATION_CHOICES = (
        ('header', 'Menú principal'),
        ('footer', 'Pie de página'),
        ('both', 'Ambos'),
    )
    
    title = models.CharField(max_length=100, verbose_name=_("Título"))
    url = models.CharField(max_length=255, verbose_name=_("URL"))
    location = models.CharField(max_length=20, choices=MENU_LOCATION_CHOICES, default='header', verbose_name=_("Ubicación"))
    order = models.PositiveIntegerField(default=0, verbose_name=_("Orden"))
    is_active = models.BooleanField(default=True, verbose_name=_("Activo"))
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children', verbose_name=_("Elemento padre"))
    
    class Meta:
        verbose_name = _("Elemento del menú")
        verbose_name_plural = _("Elementos del menú")
        ordering = ["location", "order"]
    
    def __str__(self):
        return self.title
    
    def clean(self):
        # Validar URL
        validator = URLValidator()
        try:
            validator(self.url)
        except ValidationError:
            # Si no es una URL válida, asegurarse de que sea una ruta interna válida
            if not self.url.startswith('/') and not self.url.startswith('#'):
                self.url = '/' + self.url


class Hero(TimeStampedModel):
    """
    Sección Hero de la página de inicio
    """
    title = models.CharField(max_length=200, verbose_name=_("Título"))
    subtitle = models.TextField(blank=True, verbose_name=_("Subtítulo"))
    # Tarjeta 1
    card1_icon        = models.CharField(max_length=100, verbose_name=_("Icono tarjeta 1"))
    card1_title       = models.CharField(max_length=100, verbose_name=_("Título tarjeta 1"))
    card1_description = models.TextField(verbose_name=_("Descripción tarjeta 1"))

    # Tarjeta 2
    card2_icon        = models.CharField(max_length=100, verbose_name=_("Icono tarjeta 2"))
    card2_title       = models.CharField(max_length=100, verbose_name=_("Título tarjeta 2"))
    card2_description = models.TextField(verbose_name=_("Descripción tarjeta 2"))

    # Tarjeta 3
    card3_icon        = models.CharField(max_length=100, verbose_name=_("Icono tarjeta 3"))
    card3_title       = models.CharField(max_length=100, verbose_name=_("Título tarjeta 3"))
    card3_description = models.TextField(verbose_name=_("Descripción tarjeta 3"))

    
    # Botón primario (Donar)
    primary_button_text = models.CharField(max_length=50, default="Donar", verbose_name=_("Texto botón primario"))
    primary_button_url = models.CharField(max_length=255, default="/donaciones", verbose_name=_("URL botón primario"))
    
    # Botón secundario (Conocer más)
    secondary_button_text = models.CharField(max_length=50, default="Conocer más", verbose_name=_("Texto botón secundario"))
    secondary_button_url = models.CharField(max_length=255, default="/nosotros", verbose_name=_("URL botón secundario"))
    
    #carrusel de imagenes
    
    is_active = models.BooleanField(default=True, verbose_name=_("Activo"))
    
    class Meta:
        verbose_name = _("Hero")
        verbose_name_plural = _("Heroes")
    
    def __str__(self):
        return self.title
    
class HeroCarouselImage(models.Model):
    hero      = models.ForeignKey(
        Hero,
        related_name="carousel_images",
        on_delete=models.CASCADE,
        verbose_name=_("Hero")
    )
    image     = models.ImageField(
        upload_to="home/hero_carousel/",
        verbose_name=_("Imagen")
    )
    order     = models.PositiveSmallIntegerField(
        default=0,
        verbose_name=_("Orden"),
        help_text=_("0 = primera, 1 = segunda, …")
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Activo")
    )

    class Meta:
        verbose_name        = _("Imagen del Carrusel del Hero")
        verbose_name_plural = _("Imágenes del Carrusel del Hero")
        ordering            = ["order"]

    def __str__(self):
        return f"{self.hero.title} – Img {self.order}"
    
    
class Program(TimeStampedModel):
    """
    Modelo para la sección de "Nuestros Programas" en la página de inicio
    """
    image = models.ImageField(upload_to='home/programs/', verbose_name=_("Imagen"))
    title = models.CharField(max_length=100, verbose_name=_("Título"))
    description = models.TextField(verbose_name=_("Descripción"))
    button_text = models.CharField(
        max_length=50,
        default="Conocer más",
        verbose_name=_("Texto del botón")
    )
    url = models.URLField(
        max_length=255,
        verbose_name=_("URL"),
        help_text=_("Debe incluir http:// o https://")
    )    
    order = models.PositiveIntegerField(default=0, verbose_name=_("Orden"))
    is_active = models.BooleanField(default=True, verbose_name=_("Activo"))
    
    class Meta:
        verbose_name = _("Programa")
        verbose_name_plural = _("Programas")
        ordering = ["order"]
    
    def __str__(self):
        return self.title


class Testimonial(TimeStampedModel):
    """
    Modelo para la sección de citas textuales o testimonios
    """
    name = models.CharField(max_length=100, verbose_name=_("Nombre"))
    position = models.CharField(max_length=100, verbose_name=_("Cargo"))
    quote = models.TextField(verbose_name=_("Cita"))
    image = models.ImageField(upload_to='home/testimonials/', blank=True, null=True, verbose_name=_("Imagen"))
    is_featured = models.BooleanField(default=False, verbose_name=_("Destacado"))
    order = models.PositiveIntegerField(default=0, verbose_name=_("Orden"))
    is_active = models.BooleanField(default=True, verbose_name=_("Activo"))
    
    class Meta:
        verbose_name = _("Testimonio")
        verbose_name_plural = _("Testimonios")
        ordering = ["-is_featured", "order"]
    
    def __str__(self):
        return f"{self.name} - {self.position}"


class FeaturedVideo(TimeStampedModel):
    """
    Modelo para videos destacados en la página de inicio
    """
    title = models.CharField(max_length=200, verbose_name=_("Título"))
    description = models.TextField(blank=True, verbose_name=_("Descripción"))
    youtube_id = models.CharField(max_length=20, verbose_name=_("ID de YouTube"))
    thumbnail = models.ImageField(upload_to='home/videos/', blank=True, null=True, verbose_name=_("Miniatura"))
    is_active = models.BooleanField(default=True, verbose_name=_("Activo"))
    
    class Meta:
        verbose_name = _("Video destacado")
        verbose_name_plural = _("Videos destacados")
    
    def __str__(self):
        return self.title
    
    @property
    def youtube_url(self):
        return f"https://www.youtube.com/embed/{self.youtube_id}"
    
    @property
    def youtube_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        return f"https://img.youtube.com/vi/{self.youtube_id}/hqdefault.jpg"


class HomepageSection(TimeStampedModel):
    """
    Modelo para controlar qué secciones aparecen en la página de inicio y su orden
    """
    SECTION_CHOICES = (
        ('hero', 'Hero'),
        ('programs', 'Nuestros Programas'),
        ('testimonial', 'Cita Textual'),
        ('video', 'Video Destacado'),
    )
    
    section = models.CharField(max_length=20, choices=SECTION_CHOICES, unique=True, verbose_name=_("Sección"))
    title = models.CharField(max_length=200, blank=True, verbose_name=_("Título de la sección"))
    subtitle = models.TextField(blank=True, verbose_name=_("Subtítulo de la sección"))
    order = models.PositiveIntegerField(default=0, verbose_name=_("Orden"))
    is_active = models.BooleanField(default=True, verbose_name=_("Activo"))
    
    class Meta:
        verbose_name = _("Sección de la página de inicio")
        verbose_name_plural = _("Secciones de la página de inicio")
        ordering = ["order"]
    
    def __str__(self):
        return self.get_section_display()