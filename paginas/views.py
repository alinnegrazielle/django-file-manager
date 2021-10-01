# TemplateView para criar páginas simples
from django.views.generic import TemplateView


# Classe IndexView "extends" TemplateView
class IndexView(TemplateView):
    template_name = 'paginas/home.html'
