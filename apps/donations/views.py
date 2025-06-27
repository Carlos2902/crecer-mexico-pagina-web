from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.conf import settings
from django.views import View
from .models import Donation, SiteConfiguration, DonationSuccessPage
from .forms import DonationForm
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

# Vista del formulario de donación
def donation_view(request):
    site_config = SiteConfiguration.objects.first()
    if not site_config:
        return render(request, 'error.html', {'message': 'Configuración del sitio no encontrada.'})

    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            request.session['donation_data'] = form.cleaned_data
            return redirect('donations:create_checkout_session')
    else:
        form = DonationForm()

    context = {
        'donations_config': site_config,
        'form': form,
    }
    return render(request, 'Donations/donations.html', context)


class CreateCheckoutSessionView(View):
    def get_donation_data(self, request):
        return request.session.get('donation_data')

    def get(self, request, *args, **kwargs):
        data = self.get_donation_data(request)
        if not data:
            return redirect('donations:donations')

        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        amount = max(float(data.get("amount", 1)), 1.00)  # Asegura mínimo 1 MXN

        # Guardar en la base de datos
        Donation.objects.create(
            name=name,
            email=email,
            phone=phone,
            amount=amount,
        )

        unit_amount = int(round(amount * 100))  # Stripe usa centavos

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'mxn',
                    'product_data': {'name': f"Donación de {name}"},
                    'unit_amount': unit_amount,
                },
                'quantity': 1,
            }],
            customer_email=email,
            mode='payment',
            success_url=request.build_absolute_uri(reverse('donations:success')),
            cancel_url=request.build_absolute_uri(reverse('core:home')),
            locale='en',
        )
        return redirect(session.url, code=303)


def successMsg(request):
    site_config = SiteConfiguration.objects.first()
    page = get_object_or_404(DonationSuccessPage, pk=1) 
    return render(request, 'donations/success.html', {
        'donations_config': site_config,
        'page': page,
    })

