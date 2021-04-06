import gc
import re
import tempfile
from tqdm import tqdm

from django.db import transaction

from data.models import AuxilioEmergencial, Task
from data.services.file import FileService


class AuxilioEmergencialService:
    def __init__(self):
        self.__file_service = FileService()

    @transaction.atomic
    def update_dataset(self, task, file_path):

        temp_dir = tempfile.TemporaryDirectory()

        files = self.__file_service.unzip_file(file_path, temp_dir.name)

        unziped_file = list(filter(lambda f: f.find('.csv') != -1, files))[0]

        entries = self.__file_service.read_csv(file_path=unziped_file,
                                               sep=';',
                                               decimal=',',
                                               encoding='latin1',
                                               iterate=True)

        batch = []
        count = 0

        for data in tqdm(entries, miniters=10000):
            mes_disponibilizacao = data.get('MÊS DISPONIBILIZAÇÃO')
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

            ano_mes_disponibilizacao = int(mes_disponibilizacao)
            ano_disponibilizacao = int(ano_mes_disponibilizacao / 100)
            mes_disponibilizacao = int(ano_mes_disponibilizacao % 100)

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

            batch.append(AuxilioEmergencial(**entry))

            if count == 100000:
                AuxilioEmergencial.objects.bulk_create(batch)
                batch = []
                count = 0
                gc.collect()
            else:
                count += 1

        AuxilioEmergencial.objects.bulk_create(batch)

        task.status = Task.COMPLETED

        gc.collect()

        return True
