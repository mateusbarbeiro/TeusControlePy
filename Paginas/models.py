from re import S
from django.db import models
from django.contrib.auth.models import User

TIPO_CONTAS = [
	('CC', 'Conta Corrente'),
	('CP', 'Conta Poupança',),
	('CS', 'Conta Salário'),
	('CI', 'Conta Investimentos'),
]

TIPO_MOVIMENTACOES = [
	('E', 'Entrada'),
	('S', 'Saída'),
]

# tipo_conta = models.CharField(max_length=2, choices=TIPO_CONTAS)

class Pessoa(models.Model):
	nome_completo = models.CharField(max_length=50, verbose_name='Nome Completo', help_text='Digite seu nome completo')
	cpf = models.CharField(max_length=14)
	telefone = models.CharField(max_length=15, verbose_name='Telefone', help_text='Digite seu nome telefone', null=True, blank=True)
	
	usuario = models.OneToOneField(User, on_delete=models.PROTECT)

	def __str__(self) -> str:
		return '{}'.format(self.nome_completo)

	class Meta:
		ordering = ['nome_completo']

class Banco(models.Model):
	nome = models.CharField(max_length=100)
	codigo = models.DecimalField(max_digits=9999, decimal_places=0)

	def __str__(self) -> str:
		return '{} - {}'.format(self.codigo, self.nome)

# class TipoOperacao(models.Model):
# 	nome = models.CharField(max_length=50)
# 	descricao = models.CharField(max_length=100, verbose_name="Descrição")

# 	def __str__(self) -> str:
# 		return '{}'.format(self.nome)

class Categoria(models.Model):
	nome = models.CharField(max_length=50)
	descricao = models.CharField(max_length=100, verbose_name="Descrição")
	tipo_movimetacao = models.CharField(max_length=2, choices=TIPO_MOVIMENTACOES, default="S")

	def __str__(self) -> str:
		return '{}'.format(self.nome)

class TipoConta(models.Model):
	nome = models.CharField(max_length=50)
	descricao = models.CharField(max_length=100, verbose_name="Descrição")

	def __str__(self) -> str:
		return '{} - {}'.format(self.nome, self.descricao)

class ContaBancaria(models.Model):
	banco = models.ForeignKey(Banco, on_delete=models.PROTECT)
	tipo_conta = models.ForeignKey(TipoConta, on_delete=models.PROTECT)
	agencia = models.CharField(verbose_name='Agência', max_length=50)
	conta = models.CharField(max_length=10)
	valor_total = models.DecimalField(max_digits=99999999999, decimal_places=2)
	conjunta = models.BooleanField()

	usuario = models.ForeignKey(User, on_delete=models.PROTECT)

	def __str__(self) -> str:
		return '{} - {}/{}'.format(self.banco.nome, self.agencia, self.conta)

class MovimentacaoEntrada(models.Model):
	descricao = models.CharField(max_length=100, verbose_name="Descrição")
	categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
	valor = models.DecimalField(decimal_places= 2, max_digits=50)
	cadastrado_em = models.DateTimeField(auto_now_add=True)
	atualizado_em = models.DateTimeField(auto_now=True)
		
	conta_bancaria = models.ForeignKey(ContaBancaria, verbose_name="Conta Bancária", on_delete=models.PROTECT)

	def __str__(self) -> str:
		return 'R${}: {} - {}'.format(self.valor, self.categoria, self.descricao)

class MovimentacaoSaida(models.Model):
	descricao = models.CharField(max_length=100, verbose_name="Descrição")
	categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
	valor = models.DecimalField(decimal_places= 2, max_digits=50)
	cadastrado_em = models.DateTimeField(auto_now_add=True)
	atualizado_em = models.DateTimeField(auto_now=True)
		
	conta_bancaria = models.ForeignKey(ContaBancaria, verbose_name="Conta Bancária", on_delete=models.PROTECT)

	def __str__(self) -> str:
		return 'R${}: {} - {}'.format(self.valor, self.categoria, self.descricao)

class HistoricoExtrato(models.Model):
	cadastrado_em = models.DateTimeField(auto_now_add=True)
	valor_conta_antigo = models.DecimalField(decimal_places= 2, max_digits=50)
	valor_conta_atual = models.DecimalField(decimal_places= 2, max_digits=50)
	valor_movimentacao = models.DecimalField(decimal_places= 2, max_digits=50)
	tipo_movimetacao = models.CharField(max_length=2, choices=TIPO_MOVIMENTACOES, default="S")

	conta_bancaria = models.ForeignKey(ContaBancaria, verbose_name="Conta Bancária", on_delete=models.CASCADE)

	def __str__(self) -> str:
		return 'Valor de {} - R${}, saldo da conta era R${}, passou a ser R${}'.format(self.get_tipo_movimetacao_display(), 
			self.valor_movimentacao, self.valor_conta_antigo, self.valor_conta_atual)