from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from tinymce.models import HTMLField


class QuienesSomosConfig(models.Model):
    """
    Configuración general de la página Quiénes Somos
    """
    titulo_principal = models.CharField(
        max_length=100, 
        default="Nuestro Propósito",
        help_text="Título principal de la sección"
    )
    subtitulo_principal = models.CharField(
        max_length=150, 
        default="Transformar Realidades",
        help_text="Subtítulo debajo del título principal"
    )
    descripcion_principal = models.CharField(
        max_length=200, 
        default="A Través De La Educación.",
        help_text="Descripción que acompaña al subtítulo"
    )
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Configuración Quiénes Somos"
        verbose_name_plural = "Configuración Quiénes Somos"

    def __str__(self):
        return f"Config Quiénes Somos - {self.titulo_principal}"


class Mision(models.Model):
    """
    Modelo para la sección de Misión
    """
    titulo = models.CharField(
        max_length=50, 
        default="Misión",
        help_text="Título de la sección de misión"
    )
    descripcion = HTMLField(
        help_text="Descripción detallada de la misión de la organización"
    )
    activo = models.BooleanField(default=True)
    orden = models.PositiveIntegerField(
        default=1,
        help_text="Orden de aparición en la página"
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Misión"
        verbose_name_plural = "Misión"
        ordering = ['orden']

    def __str__(self):
        return f"Misión - {self.titulo}"


class Vision(models.Model):
    """
    Modelo para la sección de Visión
    """
    titulo = models.CharField(
        max_length=50, 
        default="Visión",
        help_text="Título de la sección de visión"
    )
    descripcion = HTMLField(
        help_text="Descripción detallada de la visión de la organización"
    )
    activo = models.BooleanField(default=True)
    orden = models.PositiveIntegerField(
        default=2,
        help_text="Orden de aparición en la página"
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Visión"
        verbose_name_plural = "Visión"
        ordering = ['orden']

    def __str__(self):
        return f"Visión - {self.titulo}"


class Valor(models.Model):
    """
    Modelo para los valores de la organización
    """
    nombre = models.CharField(
        max_length=100,
        help_text="Nombre del valor (ej: Respeto a la persona y su dignidad)"
    )
    descripcion = models.TextField(
        blank=True,
        null=True,
        help_text="Descripción opcional del valor"
    )
    icono = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Clase de icono (ej: fas fa-heart) - Opcional"
    )
    activo = models.BooleanField(default=True)
    orden = models.PositiveIntegerField(
        default=1,
        help_text="Orden de aparición"
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Valor"
        verbose_name_plural = "Valores"
        ordering = ['orden', 'nombre']

    def __str__(self):
        return self.nombre


class ImagenCollage(models.Model):
    """
    Modelo para las imágenes que aparecen en los collages
    """
    SECCION_CHOICES = [
        ('mision', 'Misión'),
        ('vision_valores', 'Visión y Valores'),
    ]

    titulo = models.CharField(
        max_length=100,
        help_text="Título descriptivo de la imagen"
    )
    imagen = models.ImageField(
        upload_to='quienes_somos/collages/',
        help_text="Imagen para el collage"
    )
    alt_text = models.CharField(
        max_length=200,
        help_text="Texto alternativo para accesibilidad"
    )
    seccion = models.CharField(
        max_length=20,
        choices=SECCION_CHOICES,
        help_text="Sección donde aparecerá la imagen"
    )
    orden = models.PositiveIntegerField(
        default=1,
        help_text="Orden de aparición en el collage"
    )
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Imagen de Collage"
        verbose_name_plural = "Imágenes de Collage"
        ordering = ['seccion', 'orden']

    def __str__(self):
        return f"{self.get_seccion_display()} - {self.titulo}"


class MiembroEquipo(models.Model):
    """
    Modelo para los miembros del equipo
    """
    nombre = models.CharField(
        max_length=100,
        help_text="Nombre del miembro del equipo"
    )
    puesto = models.CharField(
        max_length=100,
        help_text="Puesto o rol en la organización"
    )
    imagen = models.ImageField(
        upload_to='quienes_somos/equipo/',
        help_text="Imagen del miembro del equipo"
    )
    frase_destacada = models.TextField(
        help_text="Frase destacada o cita representativa del miembro"
    )
    email = models.EmailField(
        blank=True,
        null=True,
        help_text="Email de contacto (opcional)"
    )
    linkedin = models.URLField(
        blank=True,
        null=True,
        help_text="Perfil de LinkedIn (opcional)"
    )
    activo = models.BooleanField(default=True)
    orden = models.PositiveIntegerField(
        default=1,
        help_text="Orden de aparición en el carrusel"
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Miembro del Equipo"
        verbose_name_plural = "Miembros del Equipo"
        ordering = ['orden', 'nombre']

    def __str__(self):
        return f"{self.nombre} - {self.puesto}"


class ObjetivoDesarrolloSostenible(models.Model):
    """
    Modelo para los Objetivos de Desarrollo Sostenible
    """
    numero = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(17)],
        help_text="Número del ODS (1-17)"
    )
    titulo = models.CharField(
        max_length=100,
        help_text="Título del objetivo (ej: Educación de Calidad)"
    )
    descripcion = models.TextField(
        help_text="Descripción de cómo el programa se alinea con este objetivo"
    )
    icono = models.ImageField(
        upload_to='quienes_somos/ods_iconos/',
        blank=True,
        null=True,
        help_text="Icono representativo del ODS (opcional)"
    )
    activo = models.BooleanField(default=True)
    orden = models.PositiveIntegerField(
        default=1,
        help_text="Orden de aparición"
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Objetivo de Desarrollo Sostenible"
        verbose_name_plural = "Objetivos de Desarrollo Sostenible"
        ordering = ['orden', 'numero']
        unique_together = ['numero']

    def __str__(self):
        return f"ODS {self.numero:02d} - {self.titulo}"




class SeccionProgramasODS(models.Model):
    """
    Configuración para la sección de Programas alineados con ODS
    """
    titulo_completo_configurable = models.CharField(
        max_length=255,
        default="Nuestros *programas* están *alineados* con el objetivo de desarrollo sostenible de la agenda 20/30 de la *ONU*",
        help_text="Escribe el título completo. Usa *palabra* para destacar el texto en verde."
    )
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Configuración Sección ODS"
        verbose_name_plural = "Configuración Sección ODS"

    def __str__(self):
        # Corregido: Ya no existen los campos anteriores. Se retorna un nombre estático.
        return "Configuración de la Sección ODS"