from django.urls import path
from .views import Index, BancoCreate, CategoriaCreate, TipoOperacaoCreate
from .views import BancoUpdate, CategoriaUpdate, TipoOperacaoUpdate
from .views import BancoDelete, CategoriaDelete, TipoOperacaoDelete
from .views import BancoList, CategoriaList, TipoOperacaoList

urlpatterns = [
	path('', Index.as_view(), name='index'),
	path('cadastrar/banco/', BancoCreate.as_view(), name='cadastrar-banco'),
	path('cadastrar/categoria/', CategoriaCreate.as_view(), name='cadastrar-categoria'),
	path('cadastrar/tipo-operacao/', TipoOperacaoCreate.as_view(), name='cadastrar-tipo-operacao'),

	path('editar/banco/<int:pk>/', BancoUpdate.as_view(), name='editar-banco'),
	path('editar/categoria/<int:pk>/', CategoriaUpdate.as_view(), name='editar-categoria'),
	path('editar/tipo-operacao/<int:pk>/', TipoOperacaoUpdate.as_view(), name='editar-tipo-operacao'),

	path('delete/banco/<int:pk>/', BancoDelete.as_view(), name='excluir-banco'),
	path('delete/categoria/<int:pk>/', CategoriaDelete.as_view(), name='excluir-categoria'),
	path('delete/tipo-operacao/<int:pk>/', TipoOperacaoDelete.as_view(), name='excluir-tipo-operacao'),

	path('listar/bancos/', BancoList.as_view(), name='listar-banco'),
	path('listar/categorias/', CategoriaList.as_view(), name='listar-categoria'),
	path('listar/tipo-operacoes/', TipoOperacaoList.as_view(), name='listar-tipo-operacao'),
]
