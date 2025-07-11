from django.contrib import admin
from .models import Donation, SiteConfiguration, DonationSuccessPage

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'amount', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)


@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Logo del sitio", {
            "fields": ("logo",),
        }),
        ("Título de Donaciones", {
            "fields": ("main_title", "main_subtitle"),
        }),
        ("Montos Sugeridos", {
            "fields": ("suggested_label", "suggested_amount_1", "suggested_amount_2", "suggested_amount_3"),
        }),
        ("Recuadro bajo Color Azul", {
            "fields": ("security_title", "security_text"),
        }),
    )



@admin.register(DonationSuccessPage)
class DonationSuccessPageAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Logo", {
            "fields": ("logo",),
        }),
        ("Encabezado Principal", {
            "fields": ("title", "subtitle"),
        }),
        ("Confirmación", {
            "fields": ("confirmation_title", "confirmation_text"),
        }),
        ("Impacto", {
            "fields": ("impact_title", "impact_bullet_1", "impact_bullet_2", "impact_bullet_3"),
        }),
        ("Seguimiento", {
            "fields": ("email_title", "email_text", "help_title", "help_text"),
        }),
        ("Redes Sociales", {
            "fields": ("share_title", "share_text", "share_text_facebook", "share_text_twitter", "share_text_whatsapp"),
        }),
    )
    