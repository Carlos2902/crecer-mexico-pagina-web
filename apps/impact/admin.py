from django.contrib import admin
from .models import (
    EstadisticasImpacto, EstadisticaPorEstado, MetricasImpacto,
    TestimonioEgresado, InformeAnual, Aliado, ConfiguracionAliados
)


@admin.register(EstadisticasImpacto)
class EstadisticasImpactoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'id']
    fields = ['titulo', 'subtitulo']
    
    def has_add_permission(self, request):
        # Solo permitir una instancia
        return not EstadisticasImpacto.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # No permitir eliminar
        return False


@admin.register(EstadisticaPorEstado)
class EstadisticaPorEstadoAdmin(admin.ModelAdmin):
    list_display = ['get_estado_display', 'total_egresados', 'egresados_hombres', 'egresados_mujeres', 'porcentaje_hombres', 'porcentaje_mujeres']
    list_editable = ['total_egresados', 'egresados_hombres', 'egresados_mujeres']
    list_filter = ['estado']
    search_fields = ['estado']
    ordering = ['estado']
    
    fieldsets = (
        ('Estado', {
            'fields': ['estado']
        }),
        ('Estadísticas de Egresados', {
            'fields': ['total_egresados', 'egresados_hombres', 'egresados_mujeres'],
            'description': 'La suma de hombres y mujeres no debe exceder el total de egresados'
        }),
    )
    
    def porcentaje_hombres(self, obj):
        return f"{obj.porcentaje_hombres}%"
    porcentaje_hombres.short_description = "% Hombres"
    
    def porcentaje_mujeres(self, obj):
        return f"{obj.porcentaje_mujeres}%"
    porcentaje_mujeres.short_description = "% Mujeres"


@admin.register(MetricasImpacto)
class MetricasImpactoAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'incremento_ingresos', 'recibio_ascenso', 'emprendi_negocio', 'continuo_estudios', 'formacion_continua']
    
    fieldsets = (
        ('Métricas de Impacto (%)', {
            'fields': [
                'incremento_ingresos',
                'recibio_ascenso', 
                'emprendi_negocio',
                'continuo_estudios',
                'formacion_continua'
            ],
            'description': 'Ingresa los porcentajes para cada métrica (0-100%)'
        }),
    )
    
    def has_add_permission(self, request):
        # Solo permitir una instancia
        return not MetricasImpacto.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # No permitir eliminar
        return False


@admin.register(TestimonioEgresado)
class TestimonioEgresadoAdmin(admin.ModelAdmin):
    list_display = ['nombre_egresado', 'programa_completado', 'activo']
    list_filter = ['activo', 'programa_completado']
    search_fields = ['nombre_egresado', 'programa_completado']
    list_editable = ['activo']
    
    fieldsets = (
        ('Información del Testimonio', {
            'fields': ['titulo', 'nombre_egresado', 'programa_completado', 'activo']
        }),
        ('Video', {
            'fields': ['video_youtube_id'],
            'description': 'Ingresa solo el ID del video de YouTube (ejemplo: para https://www.youtube.com/watch?v=dQw4w9WgXcQ ingresa: dQw4w9WgXcQ)'
        }),
        ('Contenido', {
            'fields': ['texto_testimonial']
        }),
    )
    
    def has_add_permission(self, request):
        # Solo permitir una instancia activa
        return not TestimonioEgresado.objects.filter(activo=True).exists()


@admin.register(InformeAnual)
class InformeAnualAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'año', 'fecha_publicacion', 'activo']
    list_filter = ['activo', 'año']
    search_fields = ['titulo', 'año']
    list_editable = ['activo']
    date_hierarchy = 'fecha_publicacion'
    
    fieldsets = (
        ('Información General', {
            'fields': ['titulo', 'subtitulo', 'año', 'fecha_publicacion', 'activo']
        }),
        ('Archivos', {
            'fields': ['archivo_pdf', 'imagen_portada']
        }),
        ('Botón de Acción', {
            'fields': ['texto_boton']
        }),
    )
    
    def has_add_permission(self, request):
        # Solo permitir una instancia activa
        return not InformeAnual.objects.filter(activo=True).exists()


@admin.register(Aliado)
class AliadoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'orden', 'activo']
    list_editable = ['orden', 'activo']
    list_filter = ['activo']
    search_fields = ['nombre']
    ordering = ['orden']
    
    fieldsets = (
        ('Información del Aliado', {
            'fields': ['nombre', 'logo', 'orden', 'activo']
        }),
    )


@admin.register(ConfiguracionAliados)
class ConfiguracionAliadosAdmin(admin.ModelAdmin):
    list_display = ['titulo']
    
    fieldsets = (
        ('Configuración de la Sección', {
            'fields': ['titulo', 'subtitulo']
        }),
    )
    
    def has_add_permission(self, request):
        # Solo permitir una instancia
        return not ConfiguracionAliados.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # No permitir eliminar
        return False


# Personalización del admin site
admin.site.site_header = 'Administración - Testimonio e Impacto'
admin.site.site_title = 'Admin Testimonio e Impacto'
admin.site.index_title = 'Panel de Administración'