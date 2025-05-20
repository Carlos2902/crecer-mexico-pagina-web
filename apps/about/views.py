from django.views.generic import View
from django.shortcuts import render

class AboutView(View):
    def get(self, request, *args, **kwargs):
        context = {
            # puedes agregar datos dinámicos aquí si es necesario
        }
        return render(request, 'about.html', context)