from django.contrib import admin


from .models import Banco, Pessoa, Categoria, TipoOperacao

admin.site.register(Pessoa)
admin.site.register(Banco)
admin.site.register(Categoria)
admin.site.register(TipoOperacao)

