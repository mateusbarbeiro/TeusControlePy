from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView 

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.shortcuts import get_object_or_404

from .models import Banco, Categoria, ContaBancaria, TipoOperacao, TipoConta, Movimentacao
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

class MovimentacaoCreate(LoginRequiredMixin, CreateView):
	model = Movimentacao
	fields = ['descricao', 'categoria', 'tipo_operacao', 'valor', 'data_e_hora']
	template_name = 'Paginas/form.html'
	success_url = reverse_lazy('listar-movimentacao')

class ContaBancariaCreate(LoginRequiredMixin, CreateView):
	model = ContaBancaria
	fields = ['tipo_conta', 'conjunta', 'banco', 'agencia', 'conta', 'valor_total']
	template_name = 'Paginas/form.html'
	success_url = reverse_lazy('listar-conta-bancaria')

	def form_valid(self, form):
		form.instance.usuario = self.request.user

		url = super().form_valid(form)

		# self.object.conjunta = True // acessa objeto recém persistido
		# self.object.save() // salva alteração realizada
		return url

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

class MovimentacaoUpdate(LoginRequiredMixin, UpdateView):
	model = Movimentacao
	fields = ['descricao', 'categoria', 'tipo_operacao', 'valor', 'data_e_hora']
	template_name = 'Paginas/form.html'
	success_url = reverse_lazy('listar-movimentacao')


class ContaBancariaUpdate(LoginRequiredMixin, UpdateView):
	model = ContaBancaria
	fields = ['tipo_conta', 'conjunta', 'banco', 'agencia', 'conta', 'valor_total']
	template_name = 'Paginas/form.html'
	success_url = reverse_lazy('listar-conta-bancaria')

	def get_object(self):
		self.object = get_object_or_404(ContaBancaria, pk=self.kwargs['pk'], usuario=self.request.user)
		return self.object

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

class MovimentacaoDelete(LoginRequiredMixin, DeleteView):
	model = Movimentacao
	template_name = 'Paginas/form-delete.html'
	success_url = reverse_lazy('listar-conta-bancaria')

class ContaBancariaDelete(LoginRequiredMixin, DeleteView):
	model = ContaBancaria
	template_name = 'Paginas/form-delete.html'
	success_url = reverse_lazy('listar-movimentacao')

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

class MovimentacaoList(LoginRequiredMixin, ListView):
	model = Movimentacao
	template_name = 'paginas/listas/movimentacao.html'

class ContaBancariaList(LoginRequiredMixin, ListView):
	model = Movimentacao
	template_name = 'paginas/listas/conta-bancaria.html'
	success_url = reverse_lazy('listar-conta-bancaria')

	def get_queryset(self):
		
		self.object_list = ContaBancaria.objects.filter(usuario = self.request.user)
		return self.object_list