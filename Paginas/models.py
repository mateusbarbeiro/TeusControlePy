from pydoc import describe
from django.db import models

TIPO_CONTAS = [
	('CC', 'Conta Corrente'),
	('CP', 'Conta Poupança',),
	('CS', 'Conta Salário'),
	('CI', 'Conta Investimentos'),
]

# tipo_conta = models.CharField(max_length=2, choices=TIPO_CONTAS)

class Pessoa(models.Model):
	nome_completo = models.CharField(max_length=50, verbose_name='Nome Completo', help_text='Digite seu nome completo')
	telefone = models.CharField(max_length=11, verbose_name='Telefone', help_text='Digite seu nome telefone', null=True, blank=True)

	def __str__(self) -> str:
		return '{}'.format(self.nome_completo)

	class Meta:
		ordering = ['nome_completo']

class Banco(models.Model):
	nome = models.CharField(max_length=100)
	codigo = models.DecimalField(max_digits=9999, decimal_places=0)

	def __str__(self) -> str:
		return '{} - {}'.format(self.codigo, self.nome)

class TipoOperacao(models.Model):
	nome = models.CharField(max_length=50)
	descricao = models.CharField(max_length=100, verbose_name="Descrição")

	def __str__(self) -> str:
		return '{}'.format(self.nome)

class Categoria(models.Model):
	nome = models.CharField(max_length=50)
	descricao = models.CharField(max_length=100, verbose_name="Descrição")

	def __str__(self) -> str:
		return '{}'.format(self.nome)

class TipoConta(models.Model):
	nome = models.CharField(max_length=50)
	descricao = models.CharField(max_length=100, verbose_name="Descrição")

	def __str__(self) -> str:
		return '{} - {}'.format(self.nome, descricao)