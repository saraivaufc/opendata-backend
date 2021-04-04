# -*- coding: utf-8 -*-
import gc
import re

from django.db import transaction

from data.models import AuxilioEmergencial, Task
from data.services.file import FileService


class AuxilioEmergencialService:
    def __init__(self):
        self.__file_service = FileService()

    @transaction.atomic
    def update_dataset(self, task, file_path):

        entries = self.__file_service.read_csv(file_path=file_path,
                                               sep=';',
                                               decimal=',',
                                               encoding='latin1',
                                               iterate=True)

        for data in entries:
            ano_mes_disponibilizacao = int(data.get('MÊS DISPONIBILIZAÇÃO'))
            ano_disponibilizacao = int(ano_mes_disponibilizacao / 100)
            mes_disponibilizacao = int(ano_mes_disponibilizacao % 100)
            uf = data.get('UF')
            codigo_municipio = data.get('CÓDIGO MUNICÍPIO IBGE')
            nome_municipio = data.get('NOME MUNICÍPIO')
            nis_beneficiario = data.get('NIS BENEFICIÁRIO')
            cpf_beneficiario = data.get('CPF BENEFICIÁRIO')
            nome_beneficiario = data.get('NOME BENEFICIÁRIO')
            nis_responsavel = data.get('NIS RESPONSÁVEL')
            cpf_responsavel = data.get('CPF RESPONSÁVEL')
            nome_responsavel = data.get('NOME RESPONSÁVEL')
            enquadramento = data.get('ENQUADRAMENTO')
            parcela = data.get('PARCELA')

            if parcela:
                parcela = int(re.sub("[^0-9]", "", parcela))

            observacao = data.get('OBSERVAÇÃO')
            valor_beneficio = data.get('VALOR BENEFÍCIO')

            entry = {
                'task': task,
                'ano_disponibilizacao': ano_disponibilizacao,
                'mes_disponibilizacao': mes_disponibilizacao,
                'uf': uf,
                'codigo_municipio': codigo_municipio,
                'nome_municipio': nome_municipio,
                'nis_beneficiario': nis_beneficiario,
                'cpf_beneficiario': cpf_beneficiario,
                'nome_beneficiario': nome_beneficiario,
                'nis_responsavel': nis_responsavel,
                'cpf_responsavel': cpf_responsavel,
                'nome_responsavel': nome_responsavel,
                'enquadramento': enquadramento,
                'parcela': parcela,
                'observacao': observacao,
                'valor_beneficio': valor_beneficio
            }

            AuxilioEmergencial.objects.create(**entry)

        task.status = Task.COMPLETED

        gc.collect()

        return True