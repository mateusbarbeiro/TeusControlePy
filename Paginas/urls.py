from django.urls import path

from .views import Index, BancoCreate, CategoriaCreate, TipoOperacaoCreate, TipoContaCreate, MovimentacaoCreate
from .views import BancoUpdate, CategoriaUpdate, TipoOperacaoUpdate, TipoContaUpdate, MovimentacaoUpdate
from .views import BancoDelete, CategoriaDelete, TipoOperacaoDelete, TipoContaDelete, MovimentacaoDelete
from .views import BancoList, CategoriaList, TipoOperacaoList, TipoContaList, MovimentacaoList

urlpatterns = [
	path('', Index.as_view(), name='index'),
	path('cadastrar/banco/', BancoCreate.as_view(), name='cadastrar-banco'),
	path('cadastrar/categoria/', CategoriaCreate.as_view(), name='cadastrar-categoria'),
	path('cadastrar/tipo-operacao/', TipoOperacaoCreate.as_view(), name='cadastrar-tipo-operacao'),
	path('cadastrar/tipo-conta/', TipoContaCreate.as_view(), name='cadastrar-tipo-conta'),
	path('cadastrar/movimentacao/', MovimentacaoCreate.as_view(), name='cadastrar-movimentacao'),

	path('editar/banco/<int:pk>/', BancoUpdate.as_view(), name='editar-banco'),
	path('editar/categoria/<int:pk>/', CategoriaUpdate.as_view(), name='editar-categoria'),
	path('editar/tipo-operacao/<int:pk>/', TipoOperacaoUpdate.as_view(), name='editar-tipo-operacao'),
	path('editar/tipo-conta/<int:pk>/', TipoContaUpdate.as_view(), name='editar-tipo-conta'),
	path('editar/movimentacao/<int:pk>/', MovimentacaoUpdate.as_view(), name='editar-movimentacao'),

	path('delete/banco/<int:pk>/', BancoDelete.as_view(), name='excluir-banco'),
	path('delete/categoria/<int:pk>/', CategoriaDelete.as_view(), name='excluir-categoria'),
	path('delete/tipo-operacao/<int:pk>/', TipoOperacaoDelete.as_view(), name='excluir-tipo-operacao'),
	path('delete/tipo-conta/<int:pk>/', TipoContaDelete.as_view(), name='excluir-tipo-conta'),
	path('delete/movimentacao/<int:pk>/', MovimentacaoDelete.as_view(), name='excluir-movimentacao'),

	path('listar/bancos/', BancoList.as_view(), name='listar-banco'),
	path('listar/categorias/', CategoriaList.as_view(), name='listar-categoria'),
	path('listar/tipo-operacoes/', TipoOperacaoList.as_view(), name='listar-tipo-operacao'),
	path('listar/tipo-conta/', TipoContaList.as_view(), name='listar-tipo-conta'),
	path('listar/movimentacao/', MovimentacaoList.as_view(), name='movimentacao'),
]
