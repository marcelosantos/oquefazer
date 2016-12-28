# -*- coding: utf-8 -*-

from django.test import TestCase

from .models import Atividade

class ProjetoTest(TestCase):

    atividadeMock = {'titulo': 'Fazer', 'descricao': 'Compras', 'status': 'false'}

    def test_pagina_inicial(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_adiciona_atividade(self):
        response = self.client.post('/adicionar/', self.atividadeMock)
        self.assertEqual(response.status_code, 200)

    def test_pagina_lista_atividade(self):
        response = self.client.get('/listar/')
        self.assertEqual(response.status_code, 200)

    def test_listagem_de_atividades(self):
        response = self.client.get('/listar/')
        self.assertContains(response, 'titulo')

class AtividadeModelTest(TestCase):

    def test_titulo_atividade(self):
        atividade = Atividade(titulo="Fazer Compras", descricao=None, status=None)
        self.assertEqual("Fazer Compras", atividade.titulo)

    def test_descricao_atividade(self):
        atividade = Atividade(titulo=None, descricao="Preciso fazer as compras da semana", status=None)
        self.assertEqual("Preciso fazer as compras da semana", atividade.descricao)
