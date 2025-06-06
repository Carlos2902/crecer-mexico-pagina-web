from django.contrib import admin
from django.utils.html import format_html
from .models import (
    QuienesSomosConfig, Mision, Vision, Valor, ImagenCollage,
    MiembroEquipo, ObjetivoDesarrolloSostenible, SeccionProgramasODS
)


@admin.register(QuienesSomosConfig)
class QuienesSomosConfigAdmin(admin.ModelAdmin):
    list_display = ['titulo_principal', 'subtitulo_principal', 'activo', 'fecha_actualizacion']
    list_filter = ['activo', 'fecha_creacion']
    search_fields = ['titulo_principal', 'subtitulo_principal']
    
    fieldsets = [
        ('Configuración Principal', {
            'fields': ['titulo_principal', 'subtitulo_principal', 'descripcion_principal']
        }),
        ('Estado', {
            'fields': ['activo']
        }),
    ]

    def has_add_permission(self, request):
        # Solo permitir una configuración
        return not QuienesSomosConfig.objects.exists()


@admin.register(Mision)
class MisionAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'activo', 'orden', 'fecha_actualizacion']
    list_filter = ['activo', 'fecha_creacion']
    search_fields = ['titulo', 'descripcion']
    list_editable = ['orden', 'activo']
    
    fieldsets = [
        ('Contenido', {
            'fields': ['titulo', 'descripcion']
        }),
        ('Configuración', {
            'fields': ['activo', 'orden']
        }),
    ]

    def has_add_permission(self, request):
        # Solo permitir una misión
        return not Mision.objects.exists()


@admin.register(Vision)
class VisionAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'activo', 'orden', 'fecha_actualizacion']
    list_filter = ['activo', 'fecha_creacion']
    search_fields = ['titulo', 'descripcion']
    list_editable = ['orden', 'activo']
    
    fieldsets = [
        ('Contenido', {
            'fields': ['titulo', 'descripcion']
        }),
        ('Configuración', {
            'fields': ['activo', 'orden']
        }),
    ]

    def has_add_permission(self, request):
        # Solo permitir una visión
        return not Vision.objects.exists()


@admin.register(Valor)
class ValorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'activo', 'orden', 'fecha_actualizacion']
    list_filter = ['activo', 'fecha_creacion']
    search_fields = ['nombre', 'descripcion']
    list_editable = ['orden', 'activo']
    ordering = ['orden', 'nombre']
    
    fieldsets = [
        ('Contenido', {
            'fields': ['nombre', 'descripcion']
        }),
        ('Apariencia', {
            'fields': ['icono']
        }),
        ('Configuración', {
            'fields': ['activo', 'orden']
        }),
    ]


@admin.register(ImagenCollage)
class ImagenCollageAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'seccion', 'imagen_preview', 'activo', 'orden', 'fecha_actualizacion']
    list_filter = ['seccion', 'activo', 'fecha_creacion']
    search_fields = ['titulo', 'alt_text']
    list_editable = ['orden', 'activo']
    ordering = ['seccion', 'orden']
    
    fieldsets = [
        ('Contenido', {
            'fields': ['titulo', 'imagen', 'alt_text']
        }),
        ('Ubicación', {
            'fields': ['seccion']
        }),
        ('Configuración', {
            'fields': ['activo', 'orden']
        }),
    ]

    def imagen_preview(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 5px;">',
                obj.imagen.url
            )
        return "Sin imagen"
    imagen_preview.short_description = 'Vista previa'


@admin.register(MiembroEquipo)
class MiembroEquipoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'puesto', 'imagen_preview', 'activo', 'orden', 'fecha_actualizacion']
    list_filter = ['activo', 'fecha_creacion']
    search_fields = ['nombre', 'puesto', 'frase_destacada']
    list_editable = ['orden', 'activo']
    ordering = ['orden', 'nombre']
    
    fieldsets = [
        ('Información Personal', {
            'fields': ['nombre', 'puesto', 'imagen', 'frase_destacada']
        }),
        ('Contacto', {
            'fields': ['email', 'linkedin'],
            'classes': ['collapse']
        }),
        ('Configuración', {
            'fields': ['activo', 'orden']
        }),
    ]

    def imagen_preview(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 50%;">',
                obj.imagen.url
            )
        return "Sin imagen"
    imagen_preview.short_description = 'Imagen'


@admin.register(ObjetivoDesarrolloSostenible)
class ObjetivoDesarrolloSostenibleAdmin(admin.ModelAdmin):
    list_display = ['numero_formateado', 'titulo', 'icono_preview', 'activo', 'orden', 'fecha_actualizacion']
    list_filter = ['activo', 'fecha_creacion']
    search_fields = ['titulo', 'descripcion']
    list_editable = ['orden', 'activo']
    ordering = ['orden', 'numero']
    
    fieldsets = [
        ('Identificación', {
            'fields': ['numero', 'titulo']
        }),
        ('Contenido', {
            'fields': ['descripcion']
        }),
        ('Apariencia', {
            'fields': ['icono']
        }),
        ('Configuración', {
            'fields': ['activo', 'orden']
        }),
    ]

    def numero_formateado(self, obj):
        return f"ODS {obj.numero:02d}"
    numero_formateado.short_description = 'ODS'

    def icono_preview(self, obj):
        if obj.icono:
            return format_html(
                '<img src="{}" style="width: 30px; height: 30px; object-fit: cover; border-radius: 3px;">',
                obj.icono.url
            )
        return "Sin icono"
    icono_preview.short_description = 'Icono'



# app/admin.py

import re
from django.contrib import admin
from django.utils.html import format_html, escape
from .models import SeccionProgramasODS

@admin.register(SeccionProgramasODS)
class SeccionProgramasODSAdmin(admin.ModelAdmin):
    list_display = ['titulo_completo_preview', 'activo', 'fecha_actualizacion']
    list_filter = ['activo']
    # Actualizado para buscar en el nuevo campo de título
    search_fields = ['titulo_completo_configurable']
    
    # fieldsets ajustados a la nueva estructura del modelo
    fieldsets = [
        ('Contenido de la Sección', {
            'fields': ['titulo_completo_configurable', 'activo'],
            'description': (
                "Para destacar una o varias palabras en color verde, "
                "enciérralas entre asteriscos. Ejemplo: 'Estos son mis *programas* principales'."
            )
        }),
    ]

    def titulo_completo_preview(self, obj):
        """
        Genera una vista previa del título, interpretando los asteriscos (*)
        para destacar el texto en verde.
        """
        # 1. Escapamos el texto del usuario para evitar inyección de HTML
        text = escape(obj.titulo_completo_configurable)

        # 2. Usamos una expresión regular para encontrar texto entre asteriscos
        # y reemplazarlo con el HTML deseado.
        # r'\*(.*?)\*' busca un asterisco, captura cualquier texto (no-codicioso), y busca otro asterisco.
        # r'<span style="...;">\1</span>' reemplaza todo el patrón con el span,
        # donde \1 es el texto capturado.
        formatted_text = re.sub(
            r'\*(.*?)\*',
            r'<span style="color: #28a745; font-weight: bold;">\1</span>',
            text
        )

        return format_html(formatted_text)
        
    titulo_completo_preview.short_description = 'Vista previa del título'

    def has_add_permission(self, request):
        """
        Impide que se puedan crear nuevas instancias si ya existe una.
        Esto convierte al modelo en una configuración 'singleton'.
        """
        return not SeccionProgramasODS.objects.exists()

    def has_delete_permission(self, request, obj=None):
        """
        Opcional: puedes desactivar el borrado para que la configuración
        siempre exista una vez creada.
        """
        return False

# Personalización del admin site
admin.site.site_header = "Panel de Administración - Quiénes Somos"
admin.site.site_title = "Admin Quiénes Somos"
admin.site.index_title = "Gestión de Contenido - Quiénes Somos"