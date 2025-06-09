from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.views import View
from .models import Donation, SiteConfiguration
import stripe

from .forms import DonationForm

stripe.api_key = settings.STRIPE_SECRET_KEY


# Vista que muestra el formulario
def donation_view(request):
    site_config = SiteConfiguration.objects.first()
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
            return redirect('donations:donations')  # nombre correcto de la url
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        amount = float(data.get("amount", 1))
        if amount < 1:
            amount = 1.00

        Donation.objects.create(
            name=name,
            email=email,
            phone=phone,
            amount=amount,
        )
        unit_amount = int(round(amount * 100))  # convertir a centavos

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'mxn',
                    'product_data': {
                        'name': f"Donación de {name}",
                    },
                    'unit_amount': unit_amount,
                },
                'quantity': 1,
            }],
            customer_email=email,
            mode='payment',
            success_url=request.build_absolute_uri('/donations/success/'),
            cancel_url=request.build_absolute_uri(reverse('core:home')),
            locale='en',
        )
        return redirect(session.url, code=303)



def charge(request, *args, **kwargs):
    amount = 5
    if request.method == 'POST':
        print('Data:', request.POST)
    return redirect(reverse('donations:success', args=[amount]))


def successMsg(request, *args, **kwargs):
    amount = args[0] if args else 0
    return render(request, 'Donations/success.html', {'amount': amount})


def cancelMsg(request):
    return render(request, 'Donations/cancel.html')

