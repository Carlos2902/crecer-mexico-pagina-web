from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views.generic import TemplateView
from .models import (
    ProyectosHero, ProgramasEducativos, BecasEscolares,
    ConvocatoriasDocumentos, DocumentoConvocatoria, ApoyoInstitucional
)


class ProyectosView(TemplateView):
    """Vista principal para la página de proyectos"""
    template_name = 'projects.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        try:
            # Obtener todas las secciones activas
            context['hero'] = ProyectosHero.objects.filter(activo=True).first()
            context['programas_educativos'] = ProgramasEducativos.objects.filter(activo=True).first()
            context['becas_escolares'] = BecasEscolares.objects.filter(activo=True).first()
            context['convocatorias'] = ConvocatoriasDocumentos.objects.filter(activo=True).first()
            context['apoyo_institucional'] = ApoyoInstitucional.objects.filter(activo=True).first()
            
            # Obtener tarjetas activas para programas educativos
            if context['programas_educativos']:
                context['tarjetas_programas'] = context['programas_educativos'].tarjetas_programa.filter(activo=True).order_by('orden')
            
            # Obtener documentos activos para convocatorias
            if context['convocatorias']:
                context['documentos_convocatorias'] = context['convocatorias'].documentos_convocatoria.filter(activo=True).order_by('orden')
        
        except Exception as e:
            # En caso de error, proporcionar contexto vacío
            context.update({
                'hero': None,
                'programas_educativos': None,
                'becas_escolares': None,
                'convocatorias': None,
                'apoyo_institucional': None,
                'tarjetas_programas': [],
                'documentos_convocatorias': [],
                'error': str(e)
            })
        
        return context


def ver_documento_convocatoria(request, documento_id):
    """Vista para servir archivos PDF de documentos de convocatorias"""
    documento = get_object_or_404(DocumentoConvocatoria, id=documento_id, activo=True)
    
    if not documento.archivo_pdf:
        raise Http404("Documento no encontrado")
    
    try:
        # Abrir y leer el archivo PDF
        with open(documento.archivo_pdf.path, 'rb') as pdf_file:
            response = HttpResponse(pdf_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'inline; filename="{documento.titulo}.pdf"'
            return response
    except FileNotFoundError:
        raise Http404("Archivo no encontrado")


# Vista basada en función alternativa (si prefieres este enfoque)
def proyectos_view(request):
    """Vista de función alternativa para la página de proyectos"""
    
    context = {
        'hero': ProyectosHero.objects.filter(activo=True).first(),
        'programas_educativos': ProgramasEducativos.objects.filter(activo=True).first(),
        'becas_escolares': BecasEscolares.objects.filter(activo=True).first(),
        'convocatorias': ConvocatoriasDocumentos.objects.filter(activo=True).first(),
        'apoyo_institucional': ApoyoInstitucional.objects.filter(activo=True).first(),
    }
    
    # Agregar tarjetas si existe la sección de programas educativos
    if context['programas_educativos']:
        context['tarjetas_programas'] = context['programas_educativos'].tarjetas_programa.filter(activo=True).order_by('orden')
    else:
        context['tarjetas_programas'] = []
    
    # Agregar documentos si existe la sección de convocatorias
    if context['convocatorias']:
        context['documentos_convocatorias'] = context['convocatorias'].documentos_convocatoria.filter(activo=True).order_by('orden')
    else:
        context['documentos_convocatorias'] = []
    
    return render(request, 'proyectos/proyectos.html', context)