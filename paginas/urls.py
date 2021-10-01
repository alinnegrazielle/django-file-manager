from django.urls import path

# Importando views criadas
from .views import IndexView
# from .views import CategoriaList, ArquivoList

urlpatterns = [
    path('', IndexView.as_view(), name='home'),

]
