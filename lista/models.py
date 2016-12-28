from __future__ import unicode_literals
from django.db import models
from oquefazer.settings import ARQUIVO_ATIVIDADES_JSON
import io, json, os, hashlib, uuid

class Atividade(models.Model):

    id_atividade = models.CharField(max_length=500)
    titulo = models.CharField(max_length=500)
    descricao = models.TextField()
    status = models.BooleanField()

    def __init__(self, titulo, descricao, status, id_atividade):
        self.__titulo = titulo
        self.__descricao = descricao
        self.__status = status

        if(not id_atividade):
            self.__id_atividade = hashlib.sha224( str(uuid.uuid4()) ).hexdigest()
        else:
            self.__id_atividade = id_atividade

    def adicionar(self):

        lista_de_atividades = []

        if(os.path.getsize(ARQUIVO_ATIVIDADES_JSON) > 20):
            with io.open(ARQUIVO_ATIVIDADES_JSON, 'r', encoding='utf-8') as ler_atividades:
                lista_de_atividades = json.load(ler_atividades)

        nova_atividade = {
            'id_atividade': self.id_atividade,
            'titulo': self.titulo,
            'descricao': self.descricao,
            'status': self.status
        }
        lista_de_atividades.append(nova_atividade)

        with io.open(ARQUIVO_ATIVIDADES_JSON, 'w', encoding='utf-8') as persiste_atividades:
            persiste_atividades.write(unicode(json.dumps(lista_de_atividades, ensure_ascii=True)))

        return True

    def listar(self):

        lista_de_atividades = []

        if(os.path.getsize(ARQUIVO_ATIVIDADES_JSON) > 20):
            with io.open(ARQUIVO_ATIVIDADES_JSON, 'r', encoding='utf-8') as ler_atividades:
                lista_de_atividades = json.load(ler_atividades)

        return lista_de_atividades

    def editar(self):

        lista_de_atividades = []

        if(os.path.getsize(ARQUIVO_ATIVIDADES_JSON) > 20):
            with io.open(ARQUIVO_ATIVIDADES_JSON, 'r', encoding='utf-8') as ler_atividades:
                lista_de_atividades = json.load(ler_atividades)

        nova_atividade = {
            'id_atividade': self.id_atividade,
            'titulo': self.titulo,
            'descricao': self.descricao,
            'status': self.status
        }

        for idx, atividade in enumerate(lista_de_atividades):
            if self.id_atividade == atividade['id_atividade']:
                atividade = nova_atividade
                lista_de_atividades[idx] = atividade

        with io.open(ARQUIVO_ATIVIDADES_JSON, 'w', encoding='utf-8') as persiste_atividades:
            persiste_atividades.write(unicode(json.dumps(lista_de_atividades, ensure_ascii=True)))

        return True

    def limpar(self):

        lista_de_atividades = []

        with io.open(ARQUIVO_ATIVIDADES_JSON, 'w', encoding='utf-8') as persiste_atividades:
            persiste_atividades.write(unicode(json.dumps(lista_de_atividades, ensure_ascii=True)))

        return lista_de_atividades

    def excluir(self):

        lista_de_atividades = []

        if(os.path.getsize(ARQUIVO_ATIVIDADES_JSON) > 20):
            with io.open(ARQUIVO_ATIVIDADES_JSON, 'r', encoding='utf-8') as ler_atividades:
                lista_de_atividades = json.load(ler_atividades)

        for idx, atividade in enumerate(lista_de_atividades):
            if self.id_atividade == atividade['id_atividade']:
                del lista_de_atividades[idx]

        with io.open(ARQUIVO_ATIVIDADES_JSON, 'w', encoding='utf-8') as persiste_atividades:
            persiste_atividades.write(unicode(json.dumps(lista_de_atividades, ensure_ascii=True)))

        return True

    def __str__(self):
        return self.titulo

    @property
    def id_atividade(self):
		return self.__id_atividade

    @property
    def titulo(self):
		return self.__titulo

    @property
    def descricao(self):
		return self.__descricao

    @property
    def status(self):
		return self.__status

    class Meta:
        managed = False
