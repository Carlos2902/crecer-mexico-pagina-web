from django.urls import path
from .views import donation_view, CreateCheckoutSessionView, successMsg

app_name = 'donations'

urlpatterns = [
    path('', donation_view, name='donations'),  
    path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create_checkout_session'),
    path('success/', successMsg, name='success'),
]