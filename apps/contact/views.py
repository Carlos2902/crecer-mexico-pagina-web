from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from apps.core.models import SiteConfiguration, MenuItem, SocialNetwork
from apps.contact.models import ContactInfo
from apps.contact.forms import ContactMessageForm

def contact_view(request):
    site_config = SiteConfiguration.objects.first()
    header_menu = MenuItem.objects.filter(is_active=True, location='header').order_by('order')
    footer_menu = MenuItem.objects.filter(is_active=True, location='footer').order_by('order')
    social_networks = SocialNetwork.objects.filter(is_active=True).order_by('order')
    contact_info = ContactInfo.objects.first()

    form = ContactMessageForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            contact_message = form.save()  # Guarda en la base de datos

            # Enviar correo
            email_subject = f"Nuevo mensaje de contacto: {contact_message.subject or 'Sin asunto'}"
            email_body = f"""
            Nombre: {contact_message.name}
            Correo: {contact_message.email}
            Teléfono: {contact_message.phone}
            Asunto: {contact_message.subject}

            Mensaje:
            {contact_message.message}
            """
            send_mail(
                email_subject,
                email_body,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],
                fail_silently=False,
            )

            messages.success(request, '¡Mensaje enviado exitosamente!')
            form = ContactMessageForm()  # limpia el formulario

            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Mensaje enviado exitosamente!'})

        else:
            messages.error(request, 'Por favor revisa los campos.')

    context = {
        'site_config': site_config,
        'header_menu': header_menu,
        'footer_menu': footer_menu,
        'social_networks': social_networks,
        'contact_info': contact_info,
        'form': form,
        'page_title': 'Contacto',
    }
    return render(request, 'contact.html', context)
