from django.db import models

class Donation(models.Model):
    donor_name      = models.CharField(max_length=255)
    donor_email     = models.EmailField()
    donor_phone     = models.CharField(max_length=20, blank=True, null=True)
    amount          = models.DecimalField(max_digits=10, decimal_places=2)
    currency        = models.CharField(max_length=10)
    payment_method  = models.CharField(max_length=50)
    transaction_id  = models.CharField(max_length=100, unique=True)
    donation_date   = models.DateTimeField(auto_now_add=True)
    status          = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.donor_name} - {self.amount} {self.currency}"
