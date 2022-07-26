from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from . import models
from django.utils.decorators import method_decorator

@method_decorator(login_required(login_url='perfil/'), name='dispatch')
class ListaVoos(ListView):
    model = models.Voo
    template_name = 'flights/lista.html'
    context_object_name = 'flights'

@method_decorator(login_required(login_url='perfil/'), name='dispatch')
class ListaFinanceiro(ListView):
    model = models.Financeiro
    template_name = 'flights/financeiro.html'
    context_object_name = 'financeiro'