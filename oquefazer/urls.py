"""oquefazer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from lista import views as lista_views

urlpatterns = [
    url(r'^$', lista_views.InicialView.as_view(), name='inicial'),
    url(r'^adicionar/$', lista_views.adicionar),
    url(r'^listar/$', lista_views.listar),
    url(r'^editar/$', lista_views.editar),
    url(r'^limpar/$', lista_views.limpar),
    url(r'^excluir/$', lista_views.excluir),
    url(r'^finalizar/$', lista_views.finalizar),
    url(r'^pendenciar/$', lista_views.pendenciar),
    url(r'^admin/', admin.site.urls),
]
