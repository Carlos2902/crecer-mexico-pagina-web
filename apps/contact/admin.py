from django.contrib import admin
from .models import ContactMessage, ContactInfo


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'is_processed')
    list_filter = ('is_processed', 'created_at')
    search_fields = ('name', 'email', 'message')

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):

    list_display = ('telefono', 'correo')
    fieldsets = (
        ("Textos Titulo, Subtitulo y Ubicación", {
            "fields": ("Titulo","Subtitulo"),
        }),
        ("Información de Contacto", {
            "fields": ("direccion","telefono","correo","horario"),
        }),
        ("Información de Personal", {
            "fields": ("promotora","tel_promotora","gerente_educativa","correo_gerente_educativa","gerente_operaciones","correo_gerente_operaciones",
                       "correo_servicio_social","correo_alianzas"),
        }),
        ("Información de Ubicación", {
            "fields": ("ubicacion_titulo","ubicacion_subtitulo","link_ubicacion"),
        }),
    )
    def has_add_permission(self, request):
        if ContactInfo.objects.exists():
            return False
        return super().has_add_permission(request)
    
    def save_model(self, request, obj, form, change):
         if not change and ContactInfo.objects.exists():
             # Si se intenta crear una nueva aunque no debería, bloquea
            raise Exception("Solo se permite una instancia de ContactInfo.")
         super().save_model(request, obj, form, change)