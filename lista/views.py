# -*- coding: utf-8 -*-

import io, json, os

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

from .models import Atividade

class ErroGeral(Exception):
    pass

""" Função para persistir as informações da ativiade """
def adiciona(request):

    try:

        """ Se a requisição for pelo método POST """
        if(request.method == 'POST'):

            """ Recebendo os valores do form """
            titulo = request.POST.get('titulo')
            descricao = request.POST.get('descricao')

            """ Cria um modelo de Atividade e atribui o título e descrição enviados no form """
            atividade = Atividade(titulo, descricao)

            """ Persite as informações """
            atividade.salvar()

            """ Responde com o conteúdo existente no arquivo """
            return HttpResponse(json.dumps(atividade.listar()), content_type='application/json')
        else:

            """ Se a requisição não for pelo método POST """
            return HttpResponse(json.dumps({'message':'Erro ao processar requisição'}), content_type='application/json')

    except Exception:
        raise ErroGeral("Houve um erro!")

def lista(request):

    try:

        """ Se a requisição for pelo método POST """
        if(request.method == 'GET'):

            """ Cria um modelo de Atividade """
            atividade = Atividade(None,None)

            """ Responde com o conteúdo existente no arquivo """
            return HttpResponse(json.dumps(atividade.listar()), content_type='application/json')
        else:

            """ Se a requisição não for pelo método POST """
            return HttpResponse(json.dumps({'message':'Erro ao processar requisição'}), content_type='application/json')

    except Exception:
        raise ErroGeral("Houve um erro!")

""" Definição da template inicial """
class InicialView(TemplateView):

    """ Nome do arquivo da template existente na pasta de templates """
    template_name = 'inicial.html'
