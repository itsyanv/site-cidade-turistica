from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Estado, Cidade, Ponto

from django.urls import reverse_lazy

# Create your views here.

### CREATE VIEWS ###

class EstadoCreate(CreateView):
    model = Estado
    fields = ['nmEstado', 'ufEstado']
    template_name = "cadastros/CreateForm.html"
    success_url = reverse_lazy('listar-estados')

class CidadeCreate(CreateView):
    model = Cidade
    fields = ['nmCidade', 'dddCidade', 'estado']
    template_name = "cadastros/CreateForm.html"
    success_url = reverse_lazy('listar-cidades')

class PontoCreate(CreateView):
    model = Ponto
    fields = ['nmPonto', 'hrInicio', 'hrfim', 'valor', 'cidade']
    template_name = "cadastros/CreateForm.html"
    success_url = reverse_lazy('listar-pontos')

### UPDATE VIEWS ###

class EstadoUpdate(UpdateView):
    model = Estado
    fields = ['nmEstado', 'ufEstado']
    template_name = "cadastros/CreateForm.html"
    success_url = reverse_lazy('listar-estados')


class CidadeUpdate(UpdateView):
    model = Cidade
    fields = ['nmCidade', 'dddCidade', 'estado']
    template_name = "cadastros/CreateForm.html"
    success_url = reverse_lazy('listar-cidades')


class PontoUpdate(UpdateView):
    model = Ponto
    fields = ['nmPonto', 'hrInicio', 'hrfim', 'valor', 'cidade']
    template_name = "cadastros/CreateForm.html"
    success_url = reverse_lazy('listar-pontos')

### DELETE VIEWS ###

class EstadoDelete(DeleteView):
    model = Estado
    template_name = "cadastros/DeleteForm.html"
    success_url = reverse_lazy('listar-estados')


class CidadeDelete(DeleteView):
    model = Cidade
    template_name = "cadastros/DeleteForm.html"
    success_url = reverse_lazy('listar-cidades')


class PontoDelete(DeleteView):
    model = Ponto
    template_name = "cadastros/DeleteForm.html"
    success_url = reverse_lazy('listar-pontos')

### LIST VIEWS ###

class EstadoList(ListView):
    model = Estado
    template_name = 'cadastros/Listas/Estados.html'


class CidadeList(ListView):
    model = Cidade
    template_name = 'cadastros/Listas/Cidades.html'


class PontoList(ListView):
    model = Ponto
    template_name = 'cadastros/Listas/Pontos.html'
