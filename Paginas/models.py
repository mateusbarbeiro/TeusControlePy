from django.db import models


ESTADOS = [
	('PR', 'Paraná'),
	('SP', 'São Paulo',),
	('SC', 'Santa Catarina')
]

class Cidade(models.Model):
	nome = models.CharField(max_length=100)
	estado = models.CharField(max_length=2, choices=ESTADOS)

	def __str__(self) -> str:
		return '{} - {}'.format(self.nome, self.estado)


class Pessoa(models.Model):
	nome_completo = models.CharField(max_length=50, verbose_name='Qual seu nome?', help_text='Digite seu nome completo')
	nascimento = models.DateField(verbose_name='Data de nascimento')
	email = models.EmailField(max_length=100, verbose_name='E-mail')

	cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

	def __str__(self) -> str:
		return '{} ({})'.format(self.nome_completo, self.nascimento)

	class Meta:
		ordering = ['nome_completo']

class Banco(models.Model):
	nome = models.CharField(max_length=100)
	codigo = models.DecimalField(max_digits=9999, decimal_places=0)

	def __str__(self) -> str:
		return '{} - {}'.format(self.codigo, self.nome)

class TipoConta(models.Model):
	nome = models.CharField(max_length=100)
	sigla = models.CharField(max_length=2)

	def __str__(self) -> str:
		return '{} - {}'.format(self.sigla, self.nome)