from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'voos'

urlpatterns = [
    path('', views.ListaVoos.as_view(), name="Lista"),
    path('financeiro/', views.ListaFinanceiro.as_view(), name="ListaFinanceiro")
]
