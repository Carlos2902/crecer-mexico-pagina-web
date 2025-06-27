from django.contrib import admin
from django.utils.html import format_html
from .models import (
    ProyectosHero, ProgramasEducativos, TarjetaPrograma,
    BecasEscolares, ConvocatoriasDocumentos, DocumentoConvocatoria,
    ApoyoInstitucional
)


@admin.register(ProyectosHero)
class ProyectosHeroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'activo')
    list_filter = ('activo',)
    search_fields = ('titulo', 'subtitulo')
    
    fieldsets = (
        ('Contenido Principal', {
            'fields': ('titulo', 'subtitulo', 'contenido')
        }),
        ('Configuración', {
            'fields': ('activo',),
            'classes': ('collapse',)
        }),
    )


class TarjetaProgramaInline(admin.TabularInline):
    model = TarjetaPrograma
    extra = 0
    fields = ('titulo', 'subtitulo', 'orden', 'activo')
    readonly_fields = ('preview_imagen',)
    
    def preview_imagen(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 50px;" />',
                obj.imagen.url
            )
        return "Sin imagen"
    preview_imagen.short_description = "Vista previa"


@admin.register(ProgramasEducativos)
class ProgramasEducativosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'get_num_tarjetas', 'activo')
    list_filter = ('activo',)
    search_fields = ('titulo',)
    inlines = [TarjetaProgramaInline]
    
    fieldsets = (
        ('Contenido Principal', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Configuración', {
            'fields': ('activo',),
            'classes': ('collapse',)
        }),
    )
    
    def get_num_tarjetas(self, obj):
        return obj.tarjetas_programa.count()
    get_num_tarjetas.short_description = 'Número de programas'


@admin.register(TarjetaPrograma)
class TarjetaProgramaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'seccion', 'orden', 'activo', 'preview_imagen')
    list_filter = ('seccion', 'activo')
    search_fields = ('titulo', 'subtitulo')
    list_editable = ('orden', 'activo')
    ordering = ('seccion', 'orden')
    
    fieldsets = (
        ('Contenido Frontal', {
            'fields': ('seccion', 'imagen', 'subtitulo', 'titulo', 'contenido_vinetas', 'texto_boton'),
            'description': 'Contenido que se muestra inicialmente en la tarjeta del programa'
        }),
        ('Contenido Trasero', {
            'fields': ('titulo_trasero', 'contenido_trasero_vinetas'),
            'description': 'Contenido que se muestra cuando se voltea la tarjeta del programa'
        }),
        ('Configuración', {
            'fields': ('orden', 'activo'),
            'classes': ('collapse',)
        }),
    )
    
    def preview_imagen(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 50px;" />',
                obj.imagen.url
            )
        return "Sin imagen"
    preview_imagen.short_description = "Vista previa"


@admin.register(BecasEscolares)
class BecasEscolaresAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'activo', 'preview_imagen')
    list_filter = ('activo',)
    search_fields = ('titulo', 'subtitulo')
    
    fieldsets = (
        ('Contenido Principal', {
            'fields': ('imagen', 'titulo', 'subtitulo', 'texto')
        }),
        ('Botón de Acción', {
            'fields': ('texto_boton',)
        }),
        ('Configuración', {
            'fields': ('activo',),
            'classes': ('collapse',)
        }),
    )
    
    def preview_imagen(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 50px;" />',
                obj.imagen.url
            )
        return "Sin imagen"
    preview_imagen.short_description = "Vista previa"


class DocumentoConvocatoriaInline(admin.TabularInline):
    model = DocumentoConvocatoria
    extra = 0
    fields = ('titulo', 'orden', 'activo', 'preview_imagen')
    readonly_fields = ('preview_imagen',)
    
    def preview_imagen(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 50px;" />',
                obj.imagen.url
            )
        return "Sin imagen"
    preview_imagen.short_description = "Vista previa"


@admin.register(ConvocatoriasDocumentos)
class ConvocatoriasDocumentosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'get_num_documentos', 'activo')
    list_filter = ('activo',)
    search_fields = ('titulo',)
    inlines = [DocumentoConvocatoriaInline]
    
    fieldsets = (
        ('Contenido Principal', {
            'fields': ('titulo', 'texto', 'texto_boton')
        }),
        ('Configuración', {
            'fields': ('activo',),
            'classes': ('collapse',)
        }),
    )
    
    def get_num_documentos(self, obj):
        return obj.documentos_convocatoria.count()
    get_num_documentos.short_description = 'Número de documentos'


@admin.register(DocumentoConvocatoria)
class DocumentoConvocatoriaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'seccion', 'orden', 'activo', 'preview_imagen', 'preview_pdf')
    list_filter = ('seccion', 'activo')
    search_fields = ('titulo', 'descripcion')
    list_editable = ('orden', 'activo')
    ordering = ('seccion', 'orden')
    
    fieldsets = (
        ('Contenido Principal', {
            'fields': ('seccion', 'imagen', 'titulo', 'descripcion', 'archivo_pdf')
        }),
        ('Configuración', {
            'fields': ('orden', 'activo'),
            'classes': ('collapse',)
        }),
    )
    
    def preview_imagen(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 50px;" />',
                obj.imagen.url
            )
        return "Sin imagen"
    preview_imagen.short_description = "Vista previa"
    
    def preview_pdf(self, obj):
        if obj.archivo_pdf:
            return format_html(
                '<a href="{}" target="_blank">📄 Ver PDF</a>',
                obj.archivo_pdf.url
            )
        return "Sin archivo"
    preview_pdf.short_description = "PDF"


@admin.register(ApoyoInstitucional)
class ApoyoInstitucionalAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'activo', 'preview_imagen')
    list_filter = ('activo',)
    search_fields = ('titulo',)
    
    fieldsets = (
        ('Contenido Principal', {
            'fields': ('titulo', 'texto', 'imagen')
        }),
        ('Botón de Acción', {
            'fields': ('texto_boton',)
        }),
        ('Configuración', {
            'fields': ('activo',),
            'classes': ('collapse',)
        }),
    )
    
    def preview_imagen(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 50px;" />',
                obj.imagen.url
            )
        return "Sin imagen"
    preview_imagen.short_description = "Vista previa"


# Personalización del admin site
admin.site.site_header = "Administración de Proyectos"
admin.site.site_title = "Proyectos Admin"
admin.site.index_title = "Panel de Administración - Proyectos"