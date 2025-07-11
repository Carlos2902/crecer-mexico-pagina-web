import os
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

class EstadisticasImpacto(models.Model):
    """Modelo para la sección de cifras con mapa interactivo"""
    titulo = models.CharField(max_length=200, default="Nuestro Impacto en México")
    subtitulo = models.TextField(default="Conoce el alcance de nuestro programa educativo a nivel nacional")
    
    class Meta:
        verbose_name = "Estadísticas de Impacto"
        verbose_name_plural = "Estadísticas de Impacto"
    
    def __str__(self):
        return self.titulo


class EstadisticaPorEstado(models.Model):
    """Modelo para las cifras por estado en el mapa"""
    ESTADOS_CHOICES = [
        ('aguascalientes', 'Aguascalientes'),
        ('baja_california', 'Baja California'),
        ('baja_california_sur', 'Baja California Sur'),
        ('campeche', 'Campeche'),
        ('chiapas', 'Chiapas'),
        ('chihuahua', 'Chihuahua'),
        ('coahuila', 'Coahuila'),
        ('colima', 'Colima'),
        ('durango', 'Durango'),
        ('guanajuato', 'Guanajuato'),
        ('guerrero', 'Guerrero'),
        ('hidalgo', 'Hidalgo'),
        ('jalisco', 'Jalisco'),
        ('mexico', 'Estado de México'),
        ('michoacan', 'Michoacán'),
        ('morelos', 'Morelos'),
        ('nayarit', 'Nayarit'),
        ('nuevo_leon', 'Nuevo León'),
        ('oaxaca', 'Oaxaca'),
        ('puebla', 'Puebla'),
        ('queretaro', 'Querétaro'),
        ('quintana_roo', 'Quintana Roo'),
        ('san_luis_potosi', 'San Luis Potosí'),
        ('sinaloa', 'Sinaloa'),
        ('sonora', 'Sonora'),
        ('tabasco', 'Tabasco'),
        ('tamaulipas', 'Tamaulipas'),
        ('tlaxcala', 'Tlaxcala'),
        ('veracruz', 'Veracruz'),
        ('yucatan', 'Yucatán'),
        ('zacatecas', 'Zacatecas'),
        ('cdmx', 'Ciudad de México'),
    ]
    
    estado = models.CharField(max_length=50, choices=ESTADOS_CHOICES, unique=True)
    total_egresados = models.PositiveIntegerField(default=0)
    egresados_hombres = models.PositiveIntegerField(default=0)
    egresados_mujeres = models.PositiveIntegerField(default=0)
    
    class Meta:
        verbose_name = "Estadística por Estado"
        verbose_name_plural = "Estadísticas por Estado"
        ordering = ['estado']
    
    def __str__(self):
        return f"{self.get_estado_display()}: {self.total_egresados} egresados"
    
    def clean(self):
        # Validar que la suma de hombres y mujeres no exceda el total
        if self.egresados_hombres + self.egresados_mujeres > self.total_egresados:
            raise ValidationError("La suma de hombres y mujeres no puede exceder el total de egresados")
    
    @property
    def porcentaje_hombres(self):
        if self.total_egresados == 0:
            return 0
        return round((self.egresados_hombres / self.total_egresados) * 100, 1)
    
    @property
    def porcentaje_mujeres(self):
        if self.total_egresados == 0:
            return 0
        return round((self.egresados_mujeres / self.total_egresados) * 100, 1)


class MetricasImpacto(models.Model):
    """Modelo para las 5 gráficas de anillos con métricas"""
    
    # Métricas específicas basadas en tu descripción
    incremento_ingresos = models.PositiveIntegerField(
        default=42,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Porcentaje de egresados que incrementaron sus ingresos"
    )
    
    recibio_ascenso = models.PositiveIntegerField(
        default=26,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Porcentaje de egresados que recibieron un ascenso"
    )
    
    emprendi_negocio = models.PositiveIntegerField(
        default=25,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Porcentaje de egresados que emprendieron un negocio"
    )
    
    continuo_estudios = models.PositiveIntegerField(
        default=23,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Porcentaje de egresados que continuaron estudios de media superior"
    )
    
    formacion_continua = models.PositiveIntegerField(
        default=11,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Porcentaje de egresados que se inscribieron a cursos de formación continua"
    )
    
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Métricas de Impacto"
        verbose_name_plural = "Métricas de Impacto"
    
    def __str__(self):
        return f"Métricas de Impacto - Actualizado: {self.fecha_actualizacion.strftime('%d/%m/%Y')}"


class TestimonioEgresado(models.Model):
    """Modelo para el video testimonial de egresados"""
    titulo = models.CharField(max_length=200, default="Historias de Éxito")
    video_youtube_id = models.CharField(
        max_length=100,
        help_text="ID del video de YouTube (ejemplo: dQw4w9WgXcQ)"
    )
    texto_testimonial = models.TextField(
        help_text="Texto que acompaña al video testimonial"
    )
    nombre_egresado = models.CharField(max_length=100)
    programa_completado = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Testimonio de Egresado"
        verbose_name_plural = "Testimonios de Egresados"
    
    def __str__(self):
        return f"Testimonio de {self.nombre_egresado}"
    
    @property
    def video_url(self):
        return f"https://www.youtube.com/embed/{self.video_youtube_id}"



class CarouselImage(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name=_("Título"),
        help_text=_("Se genera automáticamente desde el nombre del archivo"),
        blank=True  # Permitir que esté vacío inicialmente
    )
    image = models.ImageField(
        upload_to="impact/carousel/",
        verbose_name=_("Imagen")
    )
    order = models.PositiveSmallIntegerField(
        default=0,
        verbose_name=_("Orden"),
        help_text=_("0 = primera, 1 = segunda, …")
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Activo")
    )

    class Meta:
        verbose_name = _("Imagen del Carrusel")
        verbose_name_plural = _("Imágenes del Carrusel")
        ordering = ["order"]

    def save(self, *args, **kwargs):
        # Auto-generar título desde el nombre del archivo
        if self.image and not self.title:
            filename = os.path.basename(self.image.name)
            # Remover extensión y reemplazar guiones/guiones bajos con espacios
            self.title = os.path.splitext(filename)[0].replace('_', ' ').replace('-', ' ').title()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} – Orden {self.order}"

class InformeAnual(models.Model):
    """Modelo para el informe anual"""
    titulo = models.CharField(max_length=200, default="Informe Anual")
    subtitulo = models.TextField(default="Conoce los resultados de nuestro trabajo durante el año")
    año = models.PositiveIntegerField(default=2024)
    archivo_pdf = models.FileField(
        upload_to='informes_anuales/',
        help_text="Archivo PDF del informe anual"
    )
    imagen_portada = models.ImageField(
        upload_to='informes_anuales/portadas/',
        help_text="Imagen de portada del informe"
    )
    texto_boton = models.CharField(max_length=50, default="LEER INFORME")
    activo = models.BooleanField(default=True)
    fecha_publicacion = models.DateField()
    
    class Meta:
        verbose_name = "Informe Anual"
        verbose_name_plural = "Informes Anuales"
        ordering = ['-año']
    
    def __str__(self):
        return f"Informe Anual {self.año}"


class Aliado(models.Model):
    """Modelo para los logos de aliados"""
    nombre = models.CharField(max_length=100)
    logo = models.ImageField(
        upload_to='aliados/',
        help_text="Logo del aliado (recomendado: formato PNG con fondo transparente)"
    )
    orden = models.PositiveIntegerField(
        default=1,
        help_text="Orden de aparición en la página"
    )
    activo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Aliado"
        verbose_name_plural = "Aliados"
        ordering = ['orden']
    
    def __str__(self):
        return self.nombre


class ConfiguracionAliados(models.Model):
    """Modelo para la configuración de la sección de aliados"""
    titulo = models.CharField(max_length=200, default="Nuestros Aliados")
    subtitulo = models.TextField(
        blank=True,
        help_text="Subtítulo opcional para la sección de aliados"
    )
    
    class Meta:
        verbose_name = "Configuración de Aliados"
        verbose_name_plural = "Configuración de Aliados"
    
    def __str__(self):
        return self.titulo

