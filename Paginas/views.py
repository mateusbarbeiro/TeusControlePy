from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView 

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from .models import Banco, Categoria, TipoOperacao, TipoConta
class Index(TemplateView): 
	template_name = "paginas/modelo.html"

class BancoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
	model = Banco
	fields = ['nome', 'codigo',]
	template_name = 'Paginas/form.html'
	success_url = reverse_lazy('listar-banco')
	group_required = u"Administrador"


class CategoriaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
	model = Categoria
	fields = ['nome', 'descricao',]
	template_name = 'Paginas/form.html'
	success_url = reverse_lazy('listar-categoria')
	group_required = u"Administrador"

class TipoOperacaoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
	model = TipoOperacao
	fields = ['nome', 'descricao',]
	template_name = 'Paginas/form.html'
	success_url = reverse_lazy('listar-tipo-operacao')
	group_required = u"Administrador"

class TipoContaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
	model = TipoConta
	fields = ['nome', 'descricao',]
	template_name = 'Paginas/form.html'
	success_url = reverse_lazy('listar-tipo-conta')
	group_required = u"Administrador"

######################################################

class BancoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
	model = Banco
	fields = ['nome', 'codigo',]
	template_name = 'Paginas/form.html'
	success_url = reverse_lazy('listar-banco')
	group_required = u"Administrador"

class CategoriaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
	model = Categoria
	fields = ['nome', 'descricao',]
	template_name = 'Paginas/form.html'
	success_url = reverse_lazy('listar-categoria')
	group_required = u"Administrador"

class TipoOperacaoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
	model = TipoOperacao
	fields = ['nome', 'descricao',]
	template_name = 'Paginas/form.html'
	success_url = reverse_lazy('listar-tipo-operacao')
	group_required = u"Administrador"

class TipoContaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
	model = TipoConta
	fields = ['nome', 'descricao',]
	template_name = 'Paginas/form.html'
	success_url = reverse_lazy('listar-tipo-conta')
	group_required = u"Administrador"

######################################################

class BancoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
	model = Banco
	template_name = 'Paginas/form-delete.html'
	success_url = reverse_lazy('listar-banco')
	group_required = u"Administrador"

class CategoriaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
	model = Categoria
	template_name = 'Paginas/form-delete.html'
	success_url = reverse_lazy('listar-categoria')
	group_required = u"Administrador"

class TipoOperacaoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
	model = TipoOperacao
	template_name = 'Paginas/form-delete.html'
	success_url = reverse_lazy('listar-tipo-operacao')
	group_required = u"Administrador"
	
class TipoContaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
	model = TipoConta
	template_name = 'Paginas/form-delete.html'
	success_url = reverse_lazy('listar-tipo-conta')
	group_required = u"Administrador"

######################################################
class BancoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
	model = Banco
	template_name = 'paginas/listas/banco.html'
	group_required = u"Administrador"

class CategoriaList(GroupRequiredMixin, LoginRequiredMixin, ListView):
	model = Categoria
	template_name = 'paginas/listas/categoria.html'
	group_required = u"Administrador"

class TipoOperacaoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
	model = TipoOperacao
	template_name = 'paginas/listas/tipo-operacao.html'
	group_required = u"Administrador"

class TipoContaList(GroupRequiredMixin, LoginRequiredMixin, ListView):
	model = TipoConta
	template_name = 'paginas/listas/tipo-conta.html'
	group_required = u"Administrador"