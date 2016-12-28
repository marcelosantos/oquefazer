# -*- coding: utf-8 -*-

import io, json

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

from .models import Atividade

""" Classe para simbolização de um erro genérico """
class ErroGeral(Exception):
    pass

""" Função para persistir as informações da atividade """
def adicionar(request):

    try:

        """ Se a requisição for pelo método POST """
        if(request.method == 'POST'):

            """ Recebendo os valores do form """
            titulo = request.POST.get('titulo')
            descricao = request.POST.get('descricao')
            status = request.POST.get('status')

            """ Cria um modelo de Atividade e atribui o título e descrição enviados no form """
            atividade = Atividade(titulo, descricao, status, None)

            """ Persite as informações """
            atividade.adicionar()

            """ Responde com o conteúdo existente no arquivo """
            return HttpResponse(json.dumps(atividade.listar()), content_type='application/json')
        else:

            """ Se a requisição não for pelo método POST """
            return HttpResponse(json.dumps({'message':'Erro ao processar requisição'}), content_type='application/json')

    except Exception, ex:
        raise ErroGeral("Houve um erro! ", ex)

def listar(request):

    try:

        """ Se a requisição for pelo método POST """
        if(request.method == 'GET'):

            """ Cria um modelo de Atividade """
            atividade = Atividade(None,None,None,None)

            """ Responde com o conteúdo existente no arquivo """
            return HttpResponse(json.dumps(atividade.listar()), content_type='application/json')
        else:

            """ Se a requisição não for pelo método POST """
            return HttpResponse(json.dumps({'message':'Erro ao processar requisição'}), content_type='application/json')

    except Exception, ex:
        raise ErroGeral("Houve um erro! ", ex)

""" Função para persistir as informações da atividade editada """
def editar(request):

    try:

        """ Se a requisição for pelo método POST e existir um id de atividade """
        if(request.method == 'POST' and request.POST.get('id_atividade')):

            """ Recebendo os valores do form """
            id_atividade = request.POST.get('id_atividade')
            titulo = request.POST.get('titulo')
            descricao = request.POST.get('descricao')
            status = request.POST.get('status')

            """ Cria um modelo de Atividade e atribui o título e descrição enviados no form """
            atividade = Atividade(titulo, descricao, status, id_atividade)

            """ Persite as informações """
            atividade.editar()

            """ Responde com o conteúdo existente no arquivo """
            return HttpResponse(json.dumps(atividade.listar()), content_type='application/json')
        else:

            """ Se a requisição não for pelo método POST """
            return HttpResponse(json.dumps({'message':'Erro ao processar requisição'}), content_type='application/json')

    except Exception, ex:
        raise ErroGeral("Houve um erro! ", ex)

""" Função para remover todas as atividades cadastradas """
def limpar(request):

    try:

        """ Se a requisição for pelo método POST """
        if(request.method == 'POST'):

            """ Cria um modelo de Atividade """
            atividade = Atividade(None,None,None,None)

            """ Remove todas as atividades """
            atividade.limpar()

            """ Responde com o conteúdo existente no arquivo """
            return HttpResponse(json.dumps(atividade.listar()), content_type='application/json')
        else:

            """ Se a requisição não for pelo método POST """
            return HttpResponse(json.dumps({'message':'Erro ao processar requisição'}), content_type='application/json')

    except Exception, ex:
        raise ErroGeral("Houve um erro! ", ex)

""" Função para excluir as informações da atividade informada """
def excluir(request):

    try:

        """ Se a requisição for pelo método POST e existir um id de atividade """
        if(request.method == 'POST' and request.POST.get('id_atividade')):

            """ Recebendo os valores do form """
            id_atividade = request.POST.get('id_atividade')

            """ Cria um modelo de Atividade e baseando-se no id da atividade enviado no form """
            atividade = Atividade(None, None, None, id_atividade)

            """ Persite as informações """
            atividade.excluir()

            """ Responde com o conteúdo existente no arquivo """
            return HttpResponse(json.dumps(atividade.listar()), content_type='application/json')
        else:

            """ Se a requisição não for pelo método POST """
            return HttpResponse(json.dumps({'message':'Erro ao processar requisição'}), content_type='application/json')

    except Exception, ex:
        raise ErroGeral("Houve um erro! ", ex)

""" Função para finalizar uma atividade """
def finalizar(request):

    try:

        """ Se a requisição for pelo método POST e existir um id de atividade """
        if(request.method == 'POST' and request.POST.get('id_atividade')):

            """ Recebendo os valores do form """
            id_atividade = request.POST.get('id_atividade')

            """ Cria um modelo de Atividade e baseando-se no id da atividade enviado no form """
            atividade = Atividade(None, None, None, id_atividade)

            """ Persite as informações """
            atividade.finalizar()

            """ Responde com o conteúdo existente no arquivo """
            return HttpResponse(json.dumps(atividade.listar()), content_type='application/json')
        else:

            """ Se a requisição não for pelo método POST """
            return HttpResponse(json.dumps({'message':'Erro ao processar requisição'}), content_type='application/json')

    except Exception, ex:
        raise ErroGeral("Houve um erro! ", ex)

""" Função para tornar uma atividade pendente novamente """
def pendenciar(request):

    try:

        """ Se a requisição for pelo método POST e existir um id de atividade """
        if(request.method == 'POST' and request.POST.get('id_atividade')):

            """ Recebendo os valores do form """
            id_atividade = request.POST.get('id_atividade')

            """ Cria um modelo de Atividade e baseando-se no id da atividade enviado no form """
            atividade = Atividade(None, None, None, id_atividade)

            """ Persite as informações """
            atividade.pendenciar()

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
