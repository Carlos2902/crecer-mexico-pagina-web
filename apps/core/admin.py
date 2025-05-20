# Register your models here.
from django.contrib import admin
from .models import Hero, HeroCarouselImage, SocialNetwork, SiteConfiguration, MenuItem,  Program, Testimonial, FeaturedVideo, HomepageSection

class HeroCarouselImageInline(admin.TabularInline):
    model      = HeroCarouselImage
    extra      = 3      # número de campos vacíos por defecto
    max_num    = 10     # opcional: límite superior
    fields     = ("order", "is_active", "image")

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    inlines = [HeroCarouselImageInline]
    list_display = ("title", "is_active")


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'order', 'is_active','created_at', 'updated_at')
    list_filter = ('is_active', 'name')
    search_fields = ('name', 'url')
    ordering = ('order',)

@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'email', 'phone', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

    def has_add_permission(self, request):
        # Evitar que se creen más de una configuración en el admin
        if SiteConfiguration.objects.exists():
            return False
        return True

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'order', 'is_active', 'parent', 'created_at', 'updated_at')
    list_filter = ('location', 'is_active')
    search_fields = ('title', 'url')
    ordering = ('location', 'order')

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "order", "created_at")
    list_filter = ("is_active",)
    search_fields = ("title", "description")

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "is_active", "order")
    list_filter = ("is_featured", "is_active")
    search_fields = ("name", "position")

@admin.register(FeaturedVideo)
class FeaturedVideoAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title", "description", "youtube_id")

@admin.register(HomepageSection)
class HomepageSectionAdmin(admin.ModelAdmin):
    list_display = ("section", "title", "order", "is_active")
    list_filter = ("is_active",)

