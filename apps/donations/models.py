from django.db import models

class Donation(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - ${self.amount}"

class SiteConfiguration(models.Model):
    site_name = models.CharField(max_length=100, default="Logo de Donaciones")
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    main_title = models.CharField(max_length=200, default="Haz una Donación", verbose_name="Titulo de Donaciones ")
    main_subtitle = models.CharField(max_length=200, default="Tu apoyo hace la diferencia. Cada contribución nos ayuda a seguir adelante con nuestra misión", verbose_name="Subtítulo de Donaciones ")
    suggested_label = models.CharField (max_length=100, default="Montos sugeridos:", verbose_name="Sección de montos sugeridos")
    suggested_amount_1 = models.DecimalField(max_digits=10, decimal_places=2, default=50.00)
    suggested_amount_2 = models.DecimalField (max_digits=10, decimal_places=2, default=100.00)
    suggested_amount_3 = models.DecimalField (max_digits=10, decimal_places=2, default=250.00)
    security_title = models.CharField(max_length=100, default="Donación Segura", verbose_name="Titulo de recuadro bajo:")
    security_text = models.CharField(max_length=250, default="Todas las transacciones están protegidas con encriptación de alta seguridad.Tu información personal y financiera está completamente segura", verbose_name="Texto de recuadro bajo:")
    
    class Meta:
            verbose_name = "Configuración de Donaciones"
    def __str__(self):
        return self.site_name
    

class DonationSuccessPage(models.Model):
    logo = models.ImageField(upload_to='logos/', null=True, blank=True, verbose_name="Logo de la página")

    # Sección Principal
    title = models.CharField(max_length=200, default="¡Donación Exitosa!", verbose_name="Título Principal")
    subtitle = models.TextField(default="Tu generosa contribución ha sido procesada correctamente. Gracias por apoyar nuestra causa.", verbose_name="Subtítulo Principal")
    
    # Tarjeta de Confirmación
    confirmation_title = models.CharField(max_length=200, default="Tu apoyo hace la diferencia", verbose_name="Título de la Confirmación")
    confirmation_text = models.TextField(default="Hemos recibido tu donación...", verbose_name="Texto de la Confirmación")

    # Lista de Impacto
    impact_title = models.CharField(max_length=200, default="Tu donación ayudará a:", verbose_name="Título del Impacto")
    impact_bullet_1 = models.CharField(max_length=255, default="Brindar apoyo directo a familias necesitadas", verbose_name="Impacto punto 1")
    impact_bullet_2 = models.CharField(max_length=255, default="Desarrollar programas educativos en comunidades", verbose_name="Impacto punto 2")
    impact_bullet_3 = models.CharField(max_length=255, default="Fortalecer nuestra misión de crecimiento social", verbose_name="Impacto punto 3")

    # Información de Seguimiento
    email_title = models.CharField(max_length=200, default="Recibo por Email", verbose_name="Título Email")
    email_text = models.CharField(max_length=255, default="Te enviaremos tu recibo fiscal en los próximos minutos", verbose_name="Texto Email")

    help_title = models.CharField(max_length=200, default="¿Necesitas ayuda?", verbose_name="Título Ayuda")
    help_text = models.CharField(max_length=255, default="Contáctanos si tienes alguna pregunta sobre tu donación", verbose_name="Texto Ayuda")

    # Redes Sociales
    share_title = models.CharField(max_length=200, default="¡Comparte nuestra causa!", verbose_name="Título Compartir")
    share_text = models.TextField(default="Ayúdanos a llegar a más personas compartiendo nuestra misión en redes sociales.", verbose_name="Texto Compartir")

    share_text_facebook = models.CharField(
        max_length=255,
        default="¡Acabo de hacer una donación para apoyar a Crecer México! Únete a esta noble causa.",
        verbose_name="Texto para compartir en Facebook"
    )

    share_text_twitter = models.CharField(
        max_length=255,
        default="¡Acabo de hacer una donación para apoyar a Crecer México! Únete a esta noble causa.",
        verbose_name="Texto para compartir en Twitter"
    )

    share_text_whatsapp = models.CharField(
        max_length=255,
        default="¡Acabo de hacer una donación para apoyar a Crecer México! Únete a esta noble causa.",
        verbose_name="Texto para compartir en WhatsApp"
    )

    def __str__(self):
        return "Contenido de la Página de Donación Exitosa"

    class Meta:
        verbose_name = "Configuración de  Donación Exitosa"
    