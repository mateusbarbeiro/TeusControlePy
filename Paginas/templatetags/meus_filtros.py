from django import template

register = template.Library()

@register.filter(name="remover")
def remover(texto, r):
	return texto.replace(r, "")

@register.filter(name="esta_no_grupo")
def esta_no_grupo(usuario, nome_grupo):
	if usuario.groups.filter(name=nome_grupo):
		return True
	else: 
		return False

@register.simple_tag(name='substituir')
def substituir(texto, encontrar, sub):
	return texto.replace(encontrar, sub)


@register.simple_tag(name="cifra_real")
def cifra_real(valor):
	return 'R$ ' + str(valor)