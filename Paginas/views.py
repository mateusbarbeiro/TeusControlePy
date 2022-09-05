from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView 

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.shortcuts import get_object_or_404

from .models import Banco, Categoria, ContaBancaria, HistoricoExtrato, TipoConta, MovimentacaoEntrada, MovimentacaoSaida
class Index(TemplateView): 
	template_name = "paginas/modelo.html"

	def get_context_data(self, *args, **kwargs):
		dados = super().get_context_data(*args, **kwargs)

		return dados
class BancoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
	model = Banco
	fields = ['nome', 'codigo',]
	template_name = 'Paginas/form.html'
	success_url = reverse_lazy('listar-banco')
	group_required = u"Administrador"

class CategoriaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
	model = Categoria
	fields = ['nome', 'descricao', 'tipo_movimetacao']
	template_name = 'Paginas/form.html'
	success_url = reverse_lazy('listar-categoria')
	group_required = u"Administrador"

# class TipoOperacaoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
# 	model = TipoOperacao
# 	fields = ['nome', 'descricao',]
# 	template_name = 'Paginas/form.html'
# 	success_url = reverse_lazy('listar-tipo-operacao')
# 	group_required = u"Administrador"

class TipoContaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
	model = TipoConta
	fields = ['nome', 'descricao',]
	template_name = 'Paginas/form.html'
	success_url = reverse_lazy('listar-tipo-conta')
	group_required = u"Administrador"

class MovimentacaoEntradaCreate(LoginRequiredMixin, CreateView):
	model = MovimentacaoEntrada
	fields = ['descricao', 'categoria', 'valor', 'conta_bancaria']
	template_name = 'Paginas/form.html'
	success_url = reverse_lazy('listar-movimentacao-entrada')

	def get_context_data(self, *args, **kwargs):
		data = super().get_context_data(**kwargs)

		data['form'].fields['conta_bancaria'].queryset = ContaBancaria.objects.filter(
			usuario = self.request.user)

		return data
	
	def form_valid(self, form) :
		url = super().form_valid(form)

		try:
			conta_total = self.object.conta_bancaria.valor_total
			conta_novo_total = self.object.conta_bancaria.valor_total + self.object.valor
			# para cada movimentação, gerar uma histórico de valores
			HistoricoExtrato.objects.create(
				valor_conta_antigo = conta_total,
				valor_conta_atual = conta_novo_total,
				valor_movimentacao = self.object.valor,
				conta_bancaria = self.object.conta_bancaria,
				tipo_movimetacao = 'E',
			)

			self.object.conta_bancaria.valor_total = conta_novo_total
			self.object.conta_bancaria.save()

		except:
			self.object.delete()
			form.add_error(None, "Ocorreu um erro ao cadastrar histórico da movimentação")
			return super().form_invalid(form)
		return url

class MovimentacaoSaidaCreate(LoginRequiredMixin, CreateView):
	model = MovimentacaoSaida
	fields = ['descricao', 'categoria', 'valor', 'conta_bancaria']
	template_name = 'Paginas/form.html'
	success_url = reverse_lazy('listar-movimentacao-saida')

	def get_context_data(self, *args, **kwargs):
		data = super().get_context_data(**kwargs)

		data['form'].fields['conta_bancaria'].queryset = ContaBancaria.objects.filter(
			usuario = self.request.user)

		return data
	
	def form_valid(self, form) :
		url = super().form_valid(form)

		try:
			conta_total = self.object.conta_bancaria.valor_total
			conta_novo_total = self.object.conta_bancaria.valor_total - self.object.valor
			# para cada movimentação, gerar uma histórico de valores
			HistoricoExtrato.objects.create(
				valor_conta_antigo = conta_total,
				valor_conta_atual = conta_novo_total,
				valor_movimentacao = self.object.valor,
				conta_bancaria = self.object.conta_bancaria,
				tipo_movimetacao = 'S',
			)

			self.object.conta_bancaria.valor_total = conta_novo_total
			self.object.conta_bancaria.save()

		except:
			self.object.delete()
			form.add_error(None, "Ocorreu um erro ao cadastrar histórico da movimentação")
			return super().form_invalid(form)
		return url


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
	fields = ['nome', 'descricao', 'tipo_movimetacao']
	template_name = 'Paginas/form.html'
	success_url = reverse_lazy('listar-categoria')
	group_required = u"Administrador"

# class TipoOperacaoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
# 	model = TipoOperacao
# 	fields = ['nome', 'descricao',]
# 	template_name = 'Paginas/form.html'
# 	success_url = reverse_lazy('listar-tipo-operacao')
# 	group_required = u"Administrador"

class TipoContaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
	model = TipoConta
	fields = ['nome', 'descricao',]
	template_name = 'Paginas/form.html'
	success_url = reverse_lazy('listar-tipo-conta')
	group_required = u"Administrador"

class MovimentacaoEntradaUpdate(LoginRequiredMixin, UpdateView):
	model = MovimentacaoEntrada
	fields = ['descricao', 'categoria', 'valor', 'conta_bancaria']
	template_name = 'Paginas/form.html'
	success_url = reverse_lazy('listar-movimentacao-entrada')

	def get_context_data(self, *args, **kwargs):
		data = super().get_context_data(**kwargs)

		data['form'].fields['conta_bancaria'].queryset = ContaBancaria.objects.filter(
			usuario = self.request.user)

		return data

	def get_object(self):
		self.object = get_object_or_404(
			MovimentacaoEntrada, 
			pk=self.kwargs['pk'], 
			conta_bancaria__usuario=self.request.user)
		return self.object	

class MovimentacaoSaidaUpdate(LoginRequiredMixin, UpdateView):
	model = MovimentacaoSaida
	fields = ['descricao', 'categoria', 'valor', 'conta_bancaria']
	template_name = 'Paginas/form.html'
	success_url = reverse_lazy('listar-movimentacao-saida')

	def get_context_data(self, *args, **kwargs):
		data = super().get_context_data(**kwargs)

		data['form'].fields['conta_bancaria'].queryset = ContaBancaria.objects.filter(
			usuario = self.request.user)

		return data

	def get_object(self):
		self.object = get_object_or_404(
			MovimentacaoSaida, 
			pk=self.kwargs['pk'], 
			conta_bancaria__usuario=self.request.user)
		return self.object	


class ContaBancariaUpdate(LoginRequiredMixin, UpdateView):
	model = ContaBancaria
	fields = ['tipo_conta', 'conjunta', 'banco', 'agencia', 'conta', 'valor_total']
	template_name = 'Paginas/form.html'
	success_url = reverse_lazy('listar-conta-bancaria')

	def get_object(self):
		self.object = get_object_or_404(
			ContaBancaria, 
			pk=self.kwargs['pk'], 
			usuario=self.request.user)
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

# class TipoOperacaoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
# 	model = TipoOperacao
# 	template_name = 'Paginas/form-delete.html'
# 	success_url = reverse_lazy('listar-tipo-operacao')
# 	group_required = u"Administrador"
	
class TipoContaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
	model = TipoConta
	template_name = 'Paginas/form-delete.html'
	success_url = reverse_lazy('listar-tipo-conta')
	group_required = u"Administrador"

class MovimentacaoEntradaDelete(LoginRequiredMixin, DeleteView):
	model = MovimentacaoEntrada
	template_name = 'Paginas/form-delete.html'
	success_url = reverse_lazy('listar-movimentacao-entrada')

	def get_object(self):
		self.object = get_object_or_404(
			MovimentacaoEntrada, 
			pk=self.kwargs['pk'], 
			conta_bancaria__usuario=self.request.user)
		return self.object

class MovimentacaoSaidaDelete(LoginRequiredMixin, DeleteView):
	model = MovimentacaoSaida
	template_name = 'Paginas/form-delete.html'
	success_url = reverse_lazy('listar-movimentacao-saida')

	def get_object(self):
		self.object = get_object_or_404(
			MovimentacaoSaida, 
			pk=self.kwargs['pk'], 
			conta_bancaria__usuario=self.request.user)
		return self.object

class ContaBancariaDelete(LoginRequiredMixin, DeleteView):
	model = ContaBancaria
	template_name = 'Paginas/form-delete.html'
	success_url = reverse_lazy('listar-conta-bancaria')

	def get_object(self):
		self.object = get_object_or_404(
			ContaBancaria, 
			pk=self.kwargs['pk'], 
			usuario=self.request.user)
		return self.object

######################################################
class BancoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
	model = Banco
	template_name = 'paginas/listas/banco.html'
	group_required = u"Administrador"

class CategoriaList(GroupRequiredMixin, LoginRequiredMixin, ListView):
	model = Categoria
	template_name = 'paginas/listas/categoria.html'
	group_required = u"Administrador"

# class TipoOperacaoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
# 	model = TipoOperacao
# 	template_name = 'paginas/listas/tipo-operacao.html'
# 	group_required = u"Administrador"

class TipoContaList(GroupRequiredMixin, LoginRequiredMixin, ListView):
	model = TipoConta
	template_name = 'paginas/listas/tipo-conta.html'
	group_required = u"Administrador"

class MovimentacaoEntradaList(LoginRequiredMixin, ListView):
	model = MovimentacaoEntrada
	template_name = 'paginas/listas/movimentacao-entrada.html'

	def get_queryset(self):
		
		self.object_list = MovimentacaoEntrada.objects.filter(
			conta_bancaria__usuario = self.request.user)
		return self.object_list

class MovimentacaoSaidaList(LoginRequiredMixin, ListView):
	model = MovimentacaoSaida
	template_name = 'paginas/listas/movimentacao-saida.html'

	def get_queryset(self):
		
		self.object_list = MovimentacaoSaida.objects.filter(
			conta_bancaria__usuario = self.request.user)
		return self.object_list

class ContaBancariaList(LoginRequiredMixin, ListView):
	model = ContaBancaria
	template_name = 'paginas/listas/conta-bancaria.html'
	success_url = reverse_lazy('listar-conta-bancaria')

	def get_queryset(self):
		
		self.object_list = ContaBancaria.objects.filter(
			usuario = self.request.user)
		return self.object_list
