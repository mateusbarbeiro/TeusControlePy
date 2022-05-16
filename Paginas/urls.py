from django.urls import path
from .views import BancoCreate, CidadeCreate, TipoContaCreate, Index
from .views import BancoUpdate, CidadeUpdate, TipoContaUpdate

urlpatterns = [
	path('', Index.as_view(), name='index'),
	path('cadastrar/cidade/', CidadeCreate.as_view(), name='cadastrar-cidade'),
	path('cadastrar/banco/', BancoCreate.as_view(), name='cadastrar-banco'),
	path('cadastrar/tipo-conta/', TipoContaCreate.as_view(), name='cadastrar-tipo-conta'),

	path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name='editar-cidade'),
	path('editar/banco/<int:pk>/', BancoUpdate.as_view(), name='editar-banco'),
	path('editar/tipo-conta/', TipoContaUpdate.as_view(), name='editar-tipo-conta'),
]
