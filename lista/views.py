# -*- coding: utf-8 -*-

import io, json

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

from .models import Atividade

""" Classe para simbolização de um erro genérico """
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
            status = request.POST.get('status')

            """ Cria um modelo de Atividade e atribui o título e descrição enviados no form """
            atividade = Atividade(titulo, descricao, status)

            """ Persite as informações """
            atividade.salvar()

            """ Responde com o conteúdo existente no arquivo """
            return HttpResponse(json.dumps(atividade.listar()), content_type='application/json')
        else:

            """ Se a requisição não for pelo método POST """
            return HttpResponse(json.dumps({'message':'Erro ao processar requisição'}), content_type='application/json')

    except Exception, ex:
        raise ErroGeral("Houve um erro! ", ex)

def lista(request):

    try:

        """ Se a requisição for pelo método POST """
        if(request.method == 'GET'):

            """ Cria um modelo de Atividade """
            atividade = Atividade(None,None,None)

            """ Responde com o conteúdo existente no arquivo """
            return HttpResponse(json.dumps(atividade.listar()), content_type='application/json')
        else:

            """ Se a requisição não for pelo método POST """
            return HttpResponse(json.dumps({'message':'Erro ao processar requisição'}), content_type='application/json')

    except Exception, ex:
        raise ErroGeral("Houve um erro! ", ex)

""" Definição da template inicial """
class InicialView(TemplateView):

    """ Nome do arquivo da template existente na pasta de templates """
    template_name = 'inicial.html'
