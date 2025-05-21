from django.contrib import admin
from django.utils.html import format_html
from .models import (
    SiteConfiguration,
    SocialNetwork,
    MenuItem,
    Hero,
    Program,
    Testimonial,
    FeaturedVideo,
    HomepageSection,
    HeroCarouselImage,
)


class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'is_active', 'order')
    list_filter = ('is_active', 'name')
    search_fields = ('name', 'url')
    list_editable = ('order', 'is_active')
    ordering = ('order',)


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1
    fk_name = 'parent'
    fields = ('title', 'url', 'location', 'order', 'is_active')


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'location', 'get_parent', 'order', 'is_active')
    list_filter = ('location', 'is_active')
    search_fields = ('title', 'url')
    list_editable = ('order', 'is_active')
    inlines = [MenuItemInline]
    
    def get_parent(self, obj):
        if obj.parent:
            return obj.parent.title
        return "-"
    get_parent.short_description = "Padre"
    
    def get_queryset(self, request):
        # Solo mostrar elementos de nivel superior en la lista principal
        qs = super().get_queryset(request)
        return qs.filter(parent__isnull=True)


class SiteConfigurationAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Información básica', {
            'fields': ('site_name', 'logo', 'logo_alt', 'favicon')
        }),
        ('Información de contacto', {
            'fields': ('email', 'phone', 'address')
        }),
        ('Textos del footer', {
            'fields': ('footer_text', 'copyright_text')
        }),
        ('SEO y Analytics', {
            'fields': ('meta_description', 'meta_keywords', 'google_analytics_id'),
            'classes': ('collapse',)
        }),
    )
    
    def has_add_permission(self, request):
        # Verificar si ya existe una configuración
        return not SiteConfiguration.objects.exists()

class HeroCarouselImageInline(admin.TabularInline):
    model = HeroCarouselImage
    extra = 1 # Número de imágenes adicionales a mostrar
    fields = ('image', 'get_image_preview', 'order', 'is_active')
    readonly_fields = ('get_image_preview',)
    
    def get_image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="auto" />', obj.image.url)
        return "Sin imagen"
    get_image_preview.short_description = "Previsualización"
    


class HeroAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_editable = ('is_active',)
    inlines = [HeroCarouselImageInline]


class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image', 'order', 'is_active')
    list_filter = ('is_active',)
    list_editable = ('order', 'is_active')
    
    def get_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="auto" />', obj.image.url)
        return "Sin imagen"
    get_image.short_description = "Imagen"


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'get_image', 'is_featured', 'order', 'is_active')
    list_filter = ('is_featured', 'is_active')
    list_editable = ('is_featured', 'order', 'is_active')
    search_fields = ('name', 'position', 'quote')
    
    def get_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="auto" />', obj.image.url)
        return "Sin imagen"
    get_image.short_description = "Imagen"


class FeaturedVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_thumbnail', 'youtube_id', 'is_active')
    list_filter = ('is_active',)
    list_editable = ('is_active',)
    search_fields = ('title', 'description', 'youtube_id')
    
    def get_thumbnail(self, obj):
        return format_html('<img src="{}" width="120" height="auto" />', obj.youtube_thumbnail)
    get_thumbnail.short_description = "Miniatura"


class HomepageSectionAdmin(admin.ModelAdmin):
    list_display = ('get_section_display', 'title', 'order', 'is_active')
    list_filter = ('is_active',)
    list_editable = ('order', 'is_active')


# Registrar los modelos en el admin
admin.site.register(SiteConfiguration, SiteConfigurationAdmin)
admin.site.register(SocialNetwork, SocialNetworkAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Hero, HeroAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(FeaturedVideo, FeaturedVideoAdmin)
admin.site.register(HomepageSection, HomepageSectionAdmin)