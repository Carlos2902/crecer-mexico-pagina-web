from django.views.generic import View
from django.shortcuts import render

class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {
            # Puedes agregar variables al contexto si lo necesitas
        }
        return render(request, 'core-inicio.html', context)