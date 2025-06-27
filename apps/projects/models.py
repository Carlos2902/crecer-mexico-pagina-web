from django.db import models
from django.core.validators import FileExtensionValidator


class ProyectosHero(models.Model):
    """Sección Hero: Título principal, subtítulo, contenido introductorio"""
    titulo = models.CharField(
        max_length=200,
        verbose_name="Título",
        help_text="Título principal de la sección"
    )
    subtitulo = models.CharField(
        max_length=300,
        verbose_name="Subtítulo",
        help_text="Subtítulo descriptivo"
    )
    contenido = models.TextField(
        verbose_name="Contenido",
        help_text="Contenido principal de la sección"
    )
    activo = models.BooleanField(
        default=True,
        verbose_name="Activo",
        help_text="Marcar para mostrar esta sección"
    )
    
    class Meta:
        verbose_name = "Proyectos - Sección Hero"
        verbose_name_plural = "Proyectos - Sección Hero"
    
    def __str__(self):
        return f"Hero: {self.titulo}"


class ProgramasEducativos(models.Model):
    """Sección Programas Educativos: Título, descripción y configuración de tarjetas"""
    titulo = models.CharField(
        max_length=200,
        verbose_name="Título",
        help_text="Título de la sección de tarjetas"
    )
    descripcion = models.TextField(
        verbose_name="Descripción",
        help_text="Breve descripción de la sección"
    )
    activo = models.BooleanField(
        default=True,
        verbose_name="Activo",
        help_text="Marcar para mostrar esta sección"
    )
    
    class Meta:
        verbose_name = "Proyectos - Programas Educativos"
        verbose_name_plural = "Proyectos - Programas Educativos"
    
    def __str__(self):
        return f"Programas Educativos: {self.titulo}"


class TarjetaPrograma(models.Model):
    """Tarjetas de programas educativos con contenido frontal y trasero"""
    seccion = models.ForeignKey(
        ProgramasEducativos,
        on_delete=models.CASCADE,
        related_name='tarjetas_programa',
        verbose_name="Sección"
    )
    
    # Contenido frontal de la tarjeta
    imagen = models.ImageField(
        upload_to='proyectos/tarjetas/',
        verbose_name="Imagen",
        help_text="Imagen principal de la tarjeta"
    )
    subtitulo = models.CharField(
        max_length=150,
        verbose_name="Subtítulo",
        help_text="Subtítulo de la tarjeta"
    )
    titulo = models.CharField(
        max_length=200,
        verbose_name="Título",
        help_text="Título principal de la tarjeta"
    )
    contenido_vinetas = models.TextField(
        verbose_name="Contenido (viñetas)",
        help_text="Escribe cada viñeta en una línea nueva. Cada línea será mostrada como un elemento de lista con bullet."
    )
    texto_boton = models.CharField(
        max_length=50,
        default="Ver más",
        verbose_name="Texto del botón",
        help_text="Texto que aparecerá en el botón de acción"
    )
    
    # Contenido trasero de la tarjeta (cuando se voltea)
    titulo_trasero = models.CharField(
        max_length=200,
        verbose_name="Título (lado trasero)",
        help_text="Título que aparece cuando se voltea la tarjeta"
    )
    contenido_trasero_vinetas = models.TextField(
        verbose_name="Contenido trasero (viñetas)",
        help_text="Contenido del lado trasero. Escribe cada viñeta en una línea nueva."
    )
    
    orden = models.PositiveIntegerField(
        default=0,
        verbose_name="Orden",
        help_text="Orden de aparición de la tarjeta"
    )
    activo = models.BooleanField(
        default=True,
        verbose_name="Activo",
        help_text="Marcar para mostrar esta tarjeta"
    )
    
    class Meta:
        verbose_name = "Tarjeta de Programa Educativo"
        verbose_name_plural = "Tarjetas de Programas Educativos"
        ordering = ['orden']
    
    def __str__(self):
        return f"Programa: {self.titulo}"
    
    def get_contenido_vinetas_list(self):
        """Retorna el contenido de viñetas como lista"""
        return [linea.strip() for linea in self.contenido_vinetas.split('\n') if linea.strip()]
    
    def get_contenido_trasero_vinetas_list(self):
        """Retorna el contenido trasero de viñetas como lista"""
        return [linea.strip() for linea in self.contenido_trasero_vinetas.split('\n') if linea.strip()]


class BecasEscolares(models.Model):
    """Sección Becas Escolares: Imagen, título, subtítulo, texto, botón"""
    imagen = models.ImageField(
        upload_to='proyectos/becas/',
        verbose_name="Imagen",
        help_text="Imagen de la sección"
    )
    titulo = models.CharField(
        max_length=200,
        verbose_name="Título",
        help_text="Título de la sección"
    )
    subtitulo = models.CharField(
        max_length=300,
        verbose_name="Subtítulo",
        help_text="Subtítulo de la sección"
    )
    texto = models.TextField(
        verbose_name="Texto",
        help_text="Contenido de texto de la sección"
    )
    texto_boton = models.CharField(
        max_length=50,
        default="Contactar",
        verbose_name="Texto del botón",
        help_text="Texto que aparecerá en el botón de contacto"
    )
    activo = models.BooleanField(
        default=True,
        verbose_name="Activo",
        help_text="Marcar para mostrar esta sección"
    )
    
    class Meta:
        verbose_name = "Proyectos - Becas Escolares"
        verbose_name_plural = "Proyectos - Becas Escolares"
    
    def __str__(self):
        return f"Becas: {self.titulo}"


class ConvocatoriasDocumentos(models.Model):
    """Sección Convocatorias: Título, texto, botón y configuración de documentos"""
    titulo = models.CharField(
        max_length=200,
        verbose_name="Título",
        help_text="Título de la sección de documentos"
    )
    texto = models.TextField(
        verbose_name="Texto",
        help_text="Texto descriptivo de la sección"
    )
    texto_boton = models.CharField(
        max_length=50,
        default="Leer",
        verbose_name="Texto del botón",
        help_text="Texto que aparecerá en los botones de los documentos"
    )
    activo = models.BooleanField(
        default=True,
        verbose_name="Activo",
        help_text="Marcar para mostrar esta sección"
    )
    
    class Meta:
        verbose_name = "Proyectos - Convocatorias y Documentos"
        verbose_name_plural = "Proyectos - Convocatorias y Documentos"
    
    def __str__(self):
        return f"Convocatorias: {self.titulo}"


class DocumentoConvocatoria(models.Model):
    """Documentos PDF de convocatorias"""
    seccion = models.ForeignKey(
        ConvocatoriasDocumentos,
        on_delete=models.CASCADE,
        related_name='documentos_convocatoria',
        verbose_name="Sección"
    )
    imagen = models.ImageField(
        upload_to='proyectos/documentos/',
        verbose_name="Imagen",
        help_text="Imagen representativa del documento"
    )
    titulo = models.CharField(
        max_length=200,
        verbose_name="Título",
        help_text="Título del documento"
    )
    descripcion = models.TextField(
        blank=True,
        verbose_name="Descripción",
        help_text="Descripción opcional del documento"
    )
    archivo_pdf = models.FileField(
        upload_to='proyectos/convocatorias/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
        verbose_name="Archivo PDF",
        help_text="Archivo PDF del documento"
    )
    orden = models.PositiveIntegerField(
        default=0,
        verbose_name="Orden",
        help_text="Orden de aparición del documento"
    )
    activo = models.BooleanField(
        default=True,
        verbose_name="Activo",
        help_text="Marcar para mostrar este documento"
    )
    
    class Meta:
        verbose_name = "Documento de Convocatoria"
        verbose_name_plural = "Documentos de Convocatorias"
        ordering = ['orden']
    
    def __str__(self):
        return f"Convocatoria: {self.titulo}"


class ApoyoInstitucional(models.Model):
    """Sección Apoyo Institucional: Título, texto, imagen, botón"""
    titulo = models.CharField(
        max_length=200,
        verbose_name="Título",
        help_text="Título de la sección"
    )
    texto = models.TextField(
        verbose_name="Texto",
        help_text="Contenido de texto de la sección"
    )
    imagen = models.ImageField(
        upload_to='proyectos/apoyo_institucional/',
        verbose_name="Imagen",
        help_text="Imagen de la sección"
    )
    texto_boton = models.CharField(
        max_length=50,
        default="Contactar",
        verbose_name="Texto del botón",
        help_text="Texto que aparecerá en el botón de contacto"
    )
    activo = models.BooleanField(
        default=True,
        verbose_name="Activo",
        help_text="Marcar para mostrar esta sección"
    )
    
    class Meta:
        verbose_name = "Proyectos - Apoyo Institucional"
        verbose_name_plural = "Proyectos - Apoyo Institucional"
    
    def __str__(self):
        return f"Apoyo Institucional: {self.titulo}"