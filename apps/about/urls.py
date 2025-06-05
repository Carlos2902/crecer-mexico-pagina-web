from django.urls import path
from .views import QuienesSomosView

urlpatterns = [
    path('', QuienesSomosView.as_view(), name='about'),
]