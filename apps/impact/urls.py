from django.urls import path
from .views import TestimonialsImpactView

urlpatterns = [
    path('', TestimonialsImpactView.as_view(), name='impact'),
]