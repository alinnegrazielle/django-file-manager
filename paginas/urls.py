from django.urls import path

# Importando views criadas
from .views import IndexView, SobreView
# from .views import CategoriaList, ArquivoList

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sobre', SobreView.as_view(), name='sobre'),

]
