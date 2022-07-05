from django.urls import path

from Paginas.models import ContaBancaria

from .views import Index, BancoCreate, CategoriaCreate, TipoContaCreate, MovimentacaoEntradaCreate, ContaBancariaCreate
from .views import BancoUpdate, CategoriaUpdate, TipoContaUpdate, MovimentacaoEntradaUpdate, ContaBancariaUpdate
from .views import BancoDelete, CategoriaDelete, TipoContaDelete, MovimentacaoEntradaDelete, ContaBancariaDelete
from .views import BancoList, CategoriaList, TipoContaList, MovimentacaoEntradaList, ContaBancariaList

urlpatterns = [
	path('', Index.as_view(), name='index'),
	path('cadastrar/banco/', BancoCreate.as_view(), name='cadastrar-banco'),
	path('cadastrar/categoria/', CategoriaCreate.as_view(), name='cadastrar-categoria'),
	# path('cadastrar/tipo-operacao/', TipoOperacaoCreate.as_view(), name='cadastrar-tipo-operacao'),
	path('cadastrar/tipo-conta/', TipoContaCreate.as_view(), name='cadastrar-tipo-conta'),
	path('cadastrar/movimentacao-entrada/', MovimentacaoEntradaCreate.as_view(), name='cadastrar-movimentacao-entrada'),
	path('cadastrar/conta-bancaria/', ContaBancariaCreate.as_view(), name='cadastrar-conta-bancaria'),

	path('editar/banco/<int:pk>/', BancoUpdate.as_view(), name='editar-banco'),
	path('editar/categoria/<int:pk>/', CategoriaUpdate.as_view(), name='editar-categoria'),
	# path('editar/tipo-operacao/<int:pk>/', TipoOperacaoUpdate.as_view(), name='editar-tipo-operacao'),
	path('editar/tipo-conta/<int:pk>/', TipoContaUpdate.as_view(), name='editar-tipo-conta'),
	path('editar/movimentacao-entrada/<int:pk>/', MovimentacaoEntradaUpdate.as_view(), name='editar-movimentacao-entrada'),
	path('editar/conta-bancaria/<int:pk>/', ContaBancariaUpdate.as_view(), name='editar-conta-bancaria'),

	path('delete/banco/<int:pk>/', BancoDelete.as_view(), name='excluir-banco'),
	path('delete/categoria/<int:pk>/', CategoriaDelete.as_view(), name='excluir-categoria'),
	# path('delete/tipo-operacao/<int:pk>/', TipoOperacaoDelete.as_view(), name='excluir-tipo-operacao'),
	path('delete/tipo-conta/<int:pk>/', TipoContaDelete.as_view(), name='excluir-tipo-conta'),
	path('delete/movimentacao-entrada/<int:pk>/', MovimentacaoEntradaDelete.as_view(), name='excluir-movimentacao-entrada'),
	path('delete/conta-bancaria/<int:pk>/', ContaBancariaDelete.as_view(), name='excluir-conta-bancaria'),

	path('listar/bancos/', BancoList.as_view(), name='listar-banco'),
	path('listar/categorias/', CategoriaList.as_view(), name='listar-categoria'),
	# path('listar/tipo-operacoes/', TipoOperacaoList.as_view(), name='listar-tipo-operacao'),
	path('listar/tipo-conta/', TipoContaList.as_view(), name='listar-tipo-conta'),
	path('listar/movimentacao-entrada/', MovimentacaoEntradaList.as_view(), name='listar-movimentacao-entrada'),
	path('listar/conta-bancaria/', ContaBancariaList.as_view(), name='listar-conta-bancaria'),
]
