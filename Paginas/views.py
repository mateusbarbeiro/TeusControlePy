from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView

from .models import Cidade, Banco, TipoConta
class Index(TemplateView): 
	template_name = "paginas/modelo.html"

class CidadeCreate(CreateView):
	model = Cidade
	fields = ['nome', 'estado',]
	template_name = 'Paginas/form.html'
	success_url = reverse_lazy('index')

class BancoCreate(CreateView):
	model = Banco
	fields = ['nome', 'codigo',]
	template_name = 'Paginas/form.html'
	success_url = reverse_lazy('index')

class TipoContaCreate(CreateView):
	model = TipoConta
	fields = ['nome', 'sigla',]
	template_name = 'Paginas/form.html'
	success_url = reverse_lazy('index')

######################################################

class CidadeUpdate(UpdateView):
	model = Cidade
	fields = ['nome', 'estado',]
	template_name = 'Paginas/form.html'
	success_url = reverse_lazy('index')

class BancoUpdate(UpdateView):
	model = Banco
	fields = ['nome', 'codigo',]
	template_name = 'Paginas/form.html'
	success_url = reverse_lazy('index')

class TipoContaUpdate(UpdateView):
	model = TipoConta
	fields = ['nome', 'sigla',]
	template_name = 'Paginas/form.html'
	success_url = reverse_lazy('index')