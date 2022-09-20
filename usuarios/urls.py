from django import views
from django.urls import path
from django.contrib.auth import views

from usuarios import views as myview

urlpatterns = [
	path('login/', views.LoginView.as_view(
		template_name='usuarios/login.html'
	), name='login'),
	path('logout/', views.LogoutView.as_view(), name='logout'),
	path('signup/', myview.RegistrarPerfil.as_view(), name='signup'),
]