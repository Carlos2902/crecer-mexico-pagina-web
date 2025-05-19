from django.urls import path
from .views import DonateView

urlpatterns = [
    path('', DonateView.as_view, name='donations'),
]