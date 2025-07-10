from django import forms
from .models import ContactMessage

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Tu nombre completo',
                'required': True,
                'id': 'nombre'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'tu@email.com',
                'required': True,
                'id': 'correo'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': '+52 123 456 7890',
                'required': True,
                'id': 'telefono'
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': '¿En qué podemos ayudarte?',
                'id': 'asunto'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Escribe tu mensaje aquí...',
                'required': True,
                'id': 'mensaje'
            }),
        }