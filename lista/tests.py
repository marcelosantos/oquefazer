# -*- coding: utf-8 -*-

from django.test import TestCase

from .models import Atividade

class ProjetoTest(TestCase):

    def test_pagina_inicial(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_adiciona_atividade(self):
        response = self.client.post('/adicionar/', {'titulo': 'Fazer', 'descricao': 'Compras'})
        self.assertEqual(response.status_code, 200)

    def test_lista_atividade(self):
        response = self.client.get('/lista/')
        self.assertEqual(response.status_code, 200)

class AtividadeModelTest(TestCase):

    def test_titulo_atividade(self):
        atividade = Atividade(titulo="Fazer Compras", descricao=None)
        self.assertEqual(str(atividade), atividade.titulo)

    def test_descricao_atividade(self):
        atividade = Atividade(titulo=None, descricao="Preciso fazer as compras da semana")
        pass

    #def test_uma_atividade(self):
    #    Atividade.objects.create(titulo="1-titulo", descricao="1-descricao")
    #    response = self.client.get('/')
    #    self.assertContains(response, '1-titulo')
    #    self.assertContains(response, '1-descricao')
