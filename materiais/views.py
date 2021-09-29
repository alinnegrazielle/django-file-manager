from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Categoria, Arquivo

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class CategoriaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Categoria
    fields = ['nome']
    template_name = 'materiais/form-categoria.html'
    success_url = reverse_lazy('listar-categorias')


class ArquivoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Arquivo
    fields = ['nome', 'descricao', 'categoria', 'arquivo']
    template_name = 'materiais/form-arquivo.html'
    success_url = reverse_lazy('inicio')

##################### UPAGENS ######################


class CategoriaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Categoria
    fields = ['nome']
    template_name = 'materiais/form-categoria.html'
    success_url = reverse_lazy('listar-categorias')


class ArquivoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Arquivo
    fields = ['nome', 'descricao', 'categoria', 'arquivo']
    template_name = 'materiais/form-arquivo.html'
    success_url = reverse_lazy('inicio')

##################### UPAGENS ######################


class CategoriaDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Categoria
    template_name = 'materiais/form-exc-cat.html'
    success_url = reverse_lazy('listar-categorias')


class ArquivoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Arquivo
    template_name = 'materiais/form-exc-arq.html'
    success_url = reverse_lazy('inicio')

##################### LISTAGENS ######################


class CategoriaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Categoria
    template_name = 'materiais/listas/categoria.html'


class ArquivoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Arquivo
    template_name = 'materiais/listas/arquivo.html'
