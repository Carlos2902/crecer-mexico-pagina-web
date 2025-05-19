from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Hero, HeroCarouselImage

class HeroCarouselImageInline(admin.TabularInline):
    model      = HeroCarouselImage
    extra      = 3      # número de campos vacíos por defecto
    max_num    = 10     # opcional: límite superior
    fields     = ("order", "is_active", "image")

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    inlines = [HeroCarouselImageInline]
    list_display = ("title", "is_active")
