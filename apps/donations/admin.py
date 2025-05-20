from django.contrib import admin
from .models import Donation

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('donor_name', 'amount', 'donation_date', 'status')
    search_fields = ('donor_name', 'transaction_id')