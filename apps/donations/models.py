from django.db import models

class Donation(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - ${self.amount}"

class SiteConfiguration(models.Model):
    site_name = models.CharField(max_length=100, default="Logo de Donations")
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)

    def __str__(self):
        return self.site_name