from django.urls import path
from .views import CategoriaCreate, ArquivoCreate
from .views import CategoriaUpdate, ArquivoUpdate
from .views import CategoriaDelete, ArquivoDelete
from .views import CategoriaList, ArquivoList

urlpatterns = [
    path('criar/categoria', CategoriaCreate.as_view(), name='criar-categoria'),
    path('upar/arquivo', ArquivoCreate.as_view(), name='upar-arquivo'),

    path('editar/categoria/<int:pk>',
         CategoriaUpdate.as_view(), name='editar-categoria'),
    path('editar/arquivo/<int:pk>', ArquivoUpdate.as_view(), name='editar-arquivo'),

    path('excluir/categoria/<int:pk>',
         CategoriaDelete.as_view(), name='excluir-categoria'),
    path('excluir/arquivo/<int:pk>',
         ArquivoDelete.as_view(), name='excluir-arquivo'),

    path('listar/categorias',
         CategoriaList.as_view(), name='listar-categorias'),
    path('listar/arquivos', ArquivoList.as_view(), name='listar-arquivos'),
]
