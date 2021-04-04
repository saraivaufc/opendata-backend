# -*- coding: utf-8 -*-
import gc
import tempfile

from dateutil.parser import parse
from django.db import transaction

from data.models import (Task, CotasParlamentares,
                         CotasParlamentaresParlamentar,
                         CotasParlamentaresFornecedor,
                         CotasParlamentaresPartido,
                         CotasParlamentaresTrecho,
                         CotasParlamentaresPassageiro,
                         CotasParlamentaresTxtDescricao)
from data.services.file import FileService


class CotasParlamentaresService:
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

        for data in entries:
            txNomeParlamentar = data.get('txNomeParlamentar')
            cpf = data.get('cpf')
            ideCadastro = data.get('ideCadastro')
            nuCarteiraParlamentar = data.get('nuCarteiraParlamentar')
            nuLegislatura = data.get('nuLegislatura')
            sgUF = data.get('sgUF')
            sgPartido = data.get('sgPartido')
            codLegislatura = data.get('codLegislatura')
            numSubCota = data.get('numSubCota')
            txtDescricao = data.get('txtDescricao')
            numEspecificacaoSubCota = data.get('numEspecificacaoSubCota')
            txtDescricaoEspecificacao = data.get('txtDescricaoEspecificacao')
            txtFornecedor = data.get('txtFornecedor')
            txtCNPJCPF = data.get('txtCNPJCPF')
            txtNumero = data.get('txtNumero')
            indTipoDocumento = data.get('indTipoDocumento')
            datEmissao = data.get('datEmissao')
            vlrDocumento = data.get('vlrDocumento')
            vlrGlosa = data.get('vlrGlosa')
            vlrLiquido = data.get('vlrLiquido')
            numMes = data.get('numMes')
            numAno = data.get('numAno')
            numParcela = data.get('numParcela')
            txtPassageiro = data.get('txtPassageiro')
            txtTrecho = data.get('txtTrecho')
            numLote = data.get('numLote')
            numRessarcimento = data.get('numRessarcimento')
            vlrRestituicao = data.get('vlrRestituicao')
            nuDeputadoId = data.get('nuDeputadoId')
            ideDocumento = data.get('ideDocumento')
            urlDocumento = data.get('urlDocumento')

            parlamentar, _ = CotasParlamentaresParlamentar.objects \
                .get_or_create(txNomeParlamentar=txNomeParlamentar,
                               cpf=cpf,
                               ideCadastro=ideCadastro,
                               nuCarteiraParlamentar=nuCarteiraParlamentar)

            partido, _ = CotasParlamentaresPartido.objects \
                .get_or_create(sgPartido=sgPartido)

            txtDescricao, _ = CotasParlamentaresTxtDescricao.objects \
                .get_or_create(txtDescricao=txtDescricao)

            fornecedor, _ = CotasParlamentaresFornecedor.objects \
                .get_or_create(txtFornecedor=txtFornecedor,
                               txtCNPJCPF=txtCNPJCPF)

            passageiro, _ = CotasParlamentaresPassageiro.objects \
                .get_or_create(txtPassageiro=txtPassageiro)

            trecho, _ = CotasParlamentaresTrecho.objects \
                .get_or_create(txtTrecho=txtTrecho)

            if datEmissao:
                try:
                    datEmissao = parse(datEmissao)
                except:
                    datEmissao = None

            entry = {
                'task': task,
                'parlamentar': parlamentar,
                'nuLegislatura': nuLegislatura,
                'sgUF': sgUF,
                'partido': partido,
                'codLegislatura': codLegislatura,
                'numSubCota': numSubCota,
                'txtDescricao': txtDescricao,
                'numEspecificacaoSubCota': numEspecificacaoSubCota,
                'txtDescricaoEspecificacao': txtDescricaoEspecificacao,
                'fornecedor': fornecedor,
                'txtNumero': txtNumero,
                'indTipoDocumento': indTipoDocumento,
                'datEmissao': datEmissao,
                'vlrDocumento': vlrDocumento,
                'vlrGlosa': vlrGlosa,
                'vlrLiquido': vlrLiquido,
                'numMes': numMes,
                'numAno': numAno,
                'numParcela': numParcela,
                'passageiro': passageiro,
                'trecho': trecho,
                'numLote': numLote,
                'numRessarcimento': numRessarcimento,
                'vlrRestituicao': vlrRestituicao,
                'nuDeputadoId': nuDeputadoId,
                'ideDocumento': ideDocumento,
                'urlDocumento': urlDocumento
            }

            CotasParlamentares.objects.create(**entry)

        task.status = Task.COMPLETED

        gc.collect()

        return True
