from django import forms

class DonationForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nombre completo')
    email = forms.EmailField(label='Correo electrónico')
    phone = forms.CharField(max_length=20, label='Teléfono')
    amount = forms.IntegerField(min_value=10, label='¿Cuánto deseas donar?')