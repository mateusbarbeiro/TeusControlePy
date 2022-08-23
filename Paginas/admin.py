from django.contrib import admin


from .models import Banco, ContaBancaria, Pessoa, Categoria, MovimentacaoEntrada, MovimentacaoSaida, HistoricoExtrato

admin.site.register(Pessoa)
admin.site.register(Banco)
admin.site.register(Categoria)
admin.site.register(MovimentacaoEntrada)
admin.site.register(ContaBancaria)
admin.site.register(MovimentacaoSaida)
admin.site.register(HistoricoExtrato)

