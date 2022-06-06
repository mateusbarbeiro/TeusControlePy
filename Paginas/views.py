from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView 

from .models import Banco, Categoria, TipoOperacao
class Index(TemplateView): 
	template_name = "paginas/modelo.html"

class BancoCreate(CreateView):
	model = Banco
	fields = ['nome', 'codigo',]
	template_name = 'Paginas/form.html'
	success_url = reverse_lazy('listar-banco')

class CategoriaCreate(CreateView):
	model = Categoria
	fields = ['nome', 'descricao',]
	template_name = 'Paginas/form.html'
	success_url = reverse_lazy('listar-tipo-operacao')

class TipoOperacaoCreate(CreateView):
	model = TipoOperacao
	fields = ['nome', 'descricao',]
	template_name = 'Paginas/form.html'
	success_url = reverse_lazy('listar-tipo-operacao')

######################################################

class BancoUpdate(UpdateView):
	model = Banco
	fields = ['nome', 'codigo',]
	template_name = 'Paginas/form.html'
	success_url = reverse_lazy('listar-banco')

class CategoriaUpdate(UpdateView):
	model = Categoria
	fields = ['nome', 'descricao',]
	template_name = 'Paginas/form.html'
	success_url = reverse_lazy('listar-categoria')

class TipoOperacaoUpdate(UpdateView):
	model = TipoOperacao
	fields = ['nome', 'descricao',]
	template_name = 'Paginas/form.html'
	success_url = reverse_lazy('listar-tipo-operacao')

######################################################

class BancoDelete(DeleteView):
	model = Banco
	template_name = 'Paginas/form-delete.html'
	success_url = reverse_lazy('listar-banco')

class CategoriaDelete(DeleteView):
	model = Categoria
	template_name = 'Paginas/form.html'
	success_url = reverse_lazy('listar-categoria')

class TipoOperacaoDelete(DeleteView):
	model = TipoOperacao
	template_name = 'Paginas/form.html'
	success_url = reverse_lazy('listar-tipo-operacao')

######################################################
class BancoList(ListView):
	model = Banco
	template_name = 'paginas/listas/banco.html'

class CategoriaList(ListView):
	model = Categoria
	template_name = 'paginas/listas/categoria.html'

class TipoOperacaoList(ListView):
	model = TipoOperacao
	template_name = 'paginas/listas/tipo-operacao.html'