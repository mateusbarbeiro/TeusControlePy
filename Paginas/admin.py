from django.contrib import admin


from .models import Banco, ContaBancaria, Pessoa, Categoria, TipoOperacao, Movimentacao

admin.site.register(Pessoa)
admin.site.register(Banco)
admin.site.register(Categoria)
admin.site.register(TipoOperacao)
admin.site.register(Movimentacao)
admin.site.register(ContaBancaria)

