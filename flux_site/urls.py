"""flux_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
#from apps.products import views as product_views
from apps.transactions import views as trans_views
from apps.clients import views as client_views
from apps.user import views as user_views

from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('teste/', views.test, name="teste"),

    # admin
    path('admin/', admin.site.urls, name="admin"),

    # index
    path('', views.index, name="index"),
    path('index', views.index, name="index"),

    # historico
    path('historico', views.history, name="history"),
    path('historico/<int:year>/<int:month>/',
         views.month_history, name="month_history"),

    # produtos
    #path('produtos/', product_views.list_products, name = "produtos"),

    # transacoes
    path('transacoes/compra/', trans_views.list_purchases, name="list_purchases"),
    path('transacoes/compra/novo',
         trans_views.create_purchase, name='create_purchase'),
    path('transacoes/venda/', trans_views.list_sales, name="list_sales"),
    path('transacoes/venda/novo', trans_views.create_sale, name='create_sale'),
    path('transacoes/deletar_venda/<int:id>/',
         trans_views.delete_sale, name='delete_sale'),
    path('transacoes/deletar_compra/<int:id>/',
         trans_views.delete_purchase, name='delete_purchase'),


    # clientes
    path('clientes/', client_views.list_clients, name="list_clients"),
    path('clientes/novo', client_views.create_client, name='create_clients'),
    path('clientes/atualizar/<int:id>/', client_views.update_client, name='update_client'),
    path('clientes/deletar/<int:id>/', client_views.delete_client, name='delete_client'),
    path('clientes/perfil/<int:id>/', client_views.client_profile, name='client_profile'),
    path('clientes/arquivar/<int:id>/', client_views.archive_client, name='archive_client'),
    path('clientes/desarquivar/<int:id>/', client_views.unarchive_client, name='unarchive_client'),


    # django auth
    path('registrar/', user_views.register, name='register'),
    path('registrar/<slug:uidb64>/<slug:token>/', user_views.activate, name='activate'),
    #path('', include("django.contrib.auth.urls")),

    path('login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name=""), name="logout"),
    path('alterar-senha', user_views.password_reset_request, name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('alterar/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('alterar/pronto/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),
]

handler404 = 'flux_site.views.handler404'
handler500 = 'flux_site.views.handler500'
