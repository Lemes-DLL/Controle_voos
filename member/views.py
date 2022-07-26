from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . import models
from . import forms

class BaseSocio(View):
    template_name = 'member/login.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.socio = None

        if self.request.user.is_authenticated:
            self.socio = models.Socio.objects.filter(usuario=self.request.user).first()
            self.contexto = {
                'userform': forms.UserForm(
                    data=self.request.POST or None,
                    usuario=self.request.user,
                    instance=self.request.user,
                    ),
                'socioform': forms.SocioForm(
                    data=self.request.POST or None,
                    instance=self.socio
                    )
            }
        else:
                        self.contexto = {
                'userform': forms.UserForm(data=self.request.POST or None),
                'socioform': forms.SocioForm(data=self.request.POST or None)
            }
        self.userform = self.contexto['userform']
        self.socioform = self.contexto['socioform']

        if self.request.user.is_authenticated:
            self.template_name = 'member/atualizar.html'

        self.renderizar = render(self.request, self.template_name, self.contexto)
    
    def get(self, *args, **kwargs):
        return self.renderizar

class Criar(BaseSocio):
    def post(self, *args, **kwargs):
        if not self.userform.is_valid() or not self.socioform.is_valid():
            return self.renderizar 

        username = self.userform.cleaned_data.get('username')
        password = self.userform.cleaned_data.get('password') 
        email = self.userform.cleaned_data.get('email') 
        first_name = self.userform.cleaned_data.get('first_name')
        last_name = self.userform.cleaned_data.get('last_name')
        
        #Usuário logado
        if self.request.user.is_authenticated:
            usuario = get_object_or_404(User, username=self.request.user.username)
            usuario.username = username

            if password:
                usuario.set_password(password)

            usuario.email = email 
            usuario.first_name = first_name
            usuario.last_name = last_name
            usuario.save()

            if not self.socio:
                socio = models.Socio(**self.socioform.cleaned_data)
                socio.save()
            else:
                socio = self.socioform.save(commit=False)
                socio.usuario = usuario
                socio.save()



        else:
            usuario = self.userform.save(commit=False)
            usuario.set_password('password')
            usuario.save()

            socio = self.socioform.save(commit=False)
            socio.usuario = usuario
            socio.save()
        
        if password:
            autentica = authenticate(
                self.request,
                username=usuario,
                password=password
                )
            if autentica:
                login(self.request, user=usuario)

        messages.success(self.request, 'Seu cadastro foi atualizado com sucesso!')
        messages.success(self.request, 'Você fez login!')

        return redirect('socios:criar')
        return self.renderizar  

class Login(View):
    def post(self, *args, **kwargs):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')

        if not username or not password:
            messages.error(self.request, 'Usuário ou senha inválido')
            return redirect('socios:criar')
        
        usuario = authenticate(self.request, username=username, password=password)

        if not usuario:
            messages.error(
                self.request,
                'Usuário ou senha inválidos'
            )
            return redirect('socios:criar')
            
        login(self.request, user=usuario)
        messages.success(self.request, 'Você fez login com sucesso!')
        return redirect('voos:Lista')


class Logout(View):
    def get(self, *args, **kwargs):
        logout(self.request)
        return redirect('socios:criar')
