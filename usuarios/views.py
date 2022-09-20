# from django.contrib.auth import login, authenticate
# from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group

from Paginas.models import Pessoa
from usuarios.forms import SignUpForm

class RegistrarPerfil(CreateView):
    template_name = '../templates/usuarios/pages-register.html'
    form_class = SignUpForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        try:

            # Valida os dados e da um INSERT no banco
            url = super().form_valid(form)

            grupo = get_object_or_404(Group, name="Administrador")
            self.object.groups.add(grupo)
            self.object.save()

            # Salva
            Pessoa.objects.create(
                usuario = self.object, 
                nome_completo = form.cleaned_data['nome_completo'] ,
                cpf = form.cleaned_data['cpf'],
                telefone = form.cleaned_data['telefone'] ,
            )
        
        except:
            self.object.delete()
            form.add_error(None, "Erro ao criar usuário. Tente novamente")
            return self.form_invalid(form)
            
        # Neste ponto, exite o objeto que foi criado no banco relacional
        # self.object.codigo = hash(self.object.pk)
        # self.object.save()
        return url
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["botao"] = "Cadastrar"
        return context



# from usuarios.forms import SignUpForm

# def signup(request):
# 	if request.method == 'POST':
# 		form = SignUpForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			user.refresh_from_db()
# 			user.pessoa.nome_completo = form.cleaned_data.get('nome_completo')
# 			user.pessoa.cpf = form.cleaned_data.get('cpf')
# 			user.pessoa.telefone = form.cleaned_data.get('telefone')
# 			user.save()
# 			raw_password = form.cleaned_data.get('password1')
# 			user = authenticate(username=user.username, password=raw_password)
# 			login(request, user)
# 			return redirect('home')
# 	else:
# 		form = SignUpForm()
# 	return render(request, 'usuarios/pages-register.html', {'form': form})