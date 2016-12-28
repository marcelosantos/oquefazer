from __future__ import unicode_literals
from django.db import models
from oquefazer.settings import ATIVIDADES_JSON
import io, json, os

class Atividade(models.Model):

    titulo = models.CharField(max_length=500)
    descricao = models.TextField()

    def __init__(self, titulo, descricao):
        self.__titulo = titulo
        self.__descricao = descricao

    def salvar(self):

        lista_de_atividades = []

        if(os.path.getsize(ATIVIDADES_JSON) > 20):
            with io.open(ATIVIDADES_JSON, 'r', encoding='utf-8') as ler_atividades:
                lista_de_atividades = json.load(ler_atividades)

        nova_atividade = {
            'titulo': self.titulo,
            'descricao': self.descricao
        }
        lista_de_atividades.append(nova_atividade)

        with io.open(ATIVIDADES_JSON, 'w', encoding='utf-8') as persiste_atividades:
            persiste_atividades.write(unicode(json.dumps(lista_de_atividades, ensure_ascii=True)))

        return True

    def listar(self):

        lista_de_atividades = []

        if(os.path.getsize(ATIVIDADES_JSON) > 20):
            with io.open(ATIVIDADES_JSON, 'r', encoding='utf-8') as ler_atividades:
                lista_de_atividades = json.load(ler_atividades)

        return lista_de_atividades

    def __str__(self):
        return self.titulo

    @property
    def titulo(self):
		return self.__titulo

    @property
    def descricao(self):
		return self.__descricao

    class Meta:
        managed = False
