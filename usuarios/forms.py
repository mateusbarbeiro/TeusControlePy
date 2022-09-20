from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class SignUpForm(UserCreationForm):
	nome_completo = forms.CharField(max_length=50)
	cpf = forms.CharField(max_length=14)
	telefone = forms.CharField(max_length=15)
	
	class Meta:
		model = User
		fields = ( 'nome_completo', 'cpf', 'telefone', 'username', 'password1', 'password2', )

	def clean_cpf(self):
		cpf = self.cleaned_data['cpf']
		if User.objects.filter(pessoa__cpf=cpf).exists():
			raise ValidationError("O CPF {} já está em uso.".format(cpf))
		
		return cpf
	
	def clean_telefone(self):
		telefone = self.cleaned_data['telefone']
		if User.objects.filter(pessoa__telefone=telefone).exists():
			raise ValidationError("O telefone {} já está em uso.".format(telefone))
		
		return telefone