from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.email}) - {self.subject}"
    class Meta:
        verbose_name = "Mensajes enviados desde Pagina de Contacto"
        verbose_name_plural = "Mensajes de Contacto"


class ContactInfo(models.Model):
    Titulo = models.CharField("Titulo pagina de Contacto", max_length=50,default="Contáctanos")
    Subtitulo = models.CharField("Subtitulo pagina de Contacto", max_length=250,default="Estamos aquí para ayudarte. Envíanos un mensaje y nos pondremos en " \
    "contacto contigo lo antes posible.")
    direccion = models.TextField("Dirección",default="Av. Juárez #123, Centro Histórico\nCiudad de México, CDMX 06000")
    telefono = models.CharField("Teléfono principal", max_length=50, default="+52 55 1234 5678")
    correo = models.EmailField("Correo principal", default="contacto@crecermexico.org")
    horario = models.TextField("Horario de atención", default="Lunes a Viernes: 9:00 AM - 6:00 PM\nSábados: 9:00 AM - 2:00 PM")

    promotora = models.CharField("Promotora", max_length=100, default="Nadia Pacheco")
    tel_promotora = models.CharField("Tel. promotora", max_length=20, default="5591659457")

    promotor = models.CharField("Promotor", max_length=100, default="Hugo Garrido")
    tel_promotor = models.CharField("Tel. promotor", max_length=20, default="5539688886")

    gerente_educativa = models.CharField("Gerente educativa", max_length=100, default="Paola Quintero Villalvazo")
    correo_gerente_educativa = models.EmailField("Correo gerente educativa", default="pquintero@crecermexico.org")

    gerente_operaciones = models.CharField("Gerente operaciones", max_length=100, default="Myriam Saldivar Aguilar")
    correo_gerente_operaciones = models.EmailField("Correo gerente operaciones", default="msaldivar@crecermexico.org")

    correo_servicio_social = models.EmailField("Correo servicio social", default="amartinez@crecermexico.org")
    correo_alianzas = models.EmailField("Correo alianzas", default="mgallastegui@crecermexico.org")

    ubicacion_titulo = models.CharField ("Titulo Ubicación", max_length=100, default="Nuestra Ubicación")
    ubicacion_subtitulo = models.CharField ("Subtitulo Ubicación", max_length=150, default="Visítanos en nuestra oficina principal")
    link_ubicacion = models.URLField("Link de ubicación", default="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3764.131699869895!2d-99.1826777!3d19.3634493!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x85d1ff8c5eb77755%3A0xe6c846c7ea3e746b!2sCRECER%20M%C3%89XICO!5e0!3m2!1ses!2smx!4v1749783441103!5m2!1ses!2smx")
    def __str__(self):
        return "Información de contacto"

    class Meta:
        verbose_name = "Información de contacto"
        verbose_name_plural = "Información de contacto"
