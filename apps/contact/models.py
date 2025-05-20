from django.db import models

class ContactMessage(models.Model):
    name         = models.CharField(max_length=255)
    email        = models.EmailField()
    phone        = models.CharField(max_length=20, blank=True, null=True)
    message      = models.TextField()
    created_at   = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f"Mensaje de {self.name}"
