from django.contrib import admin
from .models import Donation, SiteConfiguration

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'amount', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)


admin.site.register(SiteConfiguration)