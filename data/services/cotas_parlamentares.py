import gc
import tempfile

from dateutil.parser import parse
from tqdm import tqdm
from django.db import transaction

from data.models import (Task, CotasParlamentares,
                         CotasParlamentaresParlamentar,
                         CotasParlamentaresFornecedor,
                         CotasParlamentaresPartido,
                         CotasParlamentaresLegislatura,
                         CotasParlamentaresUnidadeFederativa,
                         CotasParlamentaresTrecho,
                         CotasParlamentaresPassageiro,
                         CotasParlamentaresTipoDespesa)
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
                                               encoding='utf-8',
                                               iterate=True,
                                               chunksize=10000)

        batch = []
        count = 0

        parlamentares_values = []
        parlamentares_objs = []

        partidos_values = []
        partidos_objs = []

        legislaturas_values = []
        legislaturas_objs = []

        unidades_federativas_values = []
        unidades_federativas_objs = []

        tipo_despesas_values = []
        tipo_despesas_objs = []

        fornecedores_values = []
        fornecedores_objs = []

        passageiros_values = []
        passageiros_objs = []

        trechos_values = []
        trechos_objs = []

        for data in tqdm(entries, miniters=10000):
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

            parlamentar_dict = {
                'nome': txNomeParlamentar,
                'cpf': cpf,
                'id_cadastro': ideCadastro,
                'numero_carteira_parlamentar': nuCarteiraParlamentar
            }

            try:
                index = parlamentares_values.index(parlamentar_dict)
                parlamentar = parlamentares_objs[index]
            except:
                parlamentar, _ = CotasParlamentaresParlamentar.objects \
                    .select_for_update() \
                    .get_or_create(**parlamentar_dict)

                parlamentares_values.append(parlamentar_dict)
                parlamentares_objs.append(parlamentar)

            if sgPartido:
                sgPartido = sgPartido.replace('*', '')

            partido_dict = {
                'sigla': sgPartido
            }
            try:
                index = partidos_values.index(partido_dict)
                partido = partidos_objs[index]
            except:
                partido, _ = CotasParlamentaresPartido.objects \
                    .select_for_update() \
                    .get_or_create(**partido_dict)

                partidos_values.append(partido_dict)
                partidos_objs.append(partido)

            legislatura_dict = {
                'numero': nuLegislatura,
                'codigo': codLegislatura
            }
            try:
                index = legislaturas_values.index(legislatura_dict)
                legislatura = legislaturas_objs[index]
            except:
                legislatura, _ = CotasParlamentaresLegislatura.objects \
                    .select_for_update() \
                    .get_or_create(**legislatura_dict)

                legislaturas_values.append(legislatura_dict)
                legislaturas_objs.append(legislatura)

            unidade_federativa_dict = {
                'sigla': sgUF,
            }
            try:
                index = unidades_federativas_values.index(unidade_federativa_dict)
                unidade_federativa = unidades_federativas_objs[index]
            except:
                unidade_federativa, _ = CotasParlamentaresUnidadeFederativa.objects \
                    .select_for_update() \
                    .get_or_create(**unidade_federativa_dict)

                unidades_federativas_values.append(unidade_federativa_dict)
                unidades_federativas_objs.append(unidade_federativa)

            tipo_despesa_dict = {
                'numero': numSubCota,
                'descricao': txtDescricao,
                'numero_especificacao': numEspecificacaoSubCota,
                'descricao_especificacao': txtDescricaoEspecificacao
            }
            try:
                index = tipo_despesas_values.index(tipo_despesa_dict)
                tipo_despesa = tipo_despesas_objs[index]
            except:
                tipo_despesa, _ = CotasParlamentaresTipoDespesa.objects \
                    .select_for_update() \
                    .get_or_create(**tipo_despesa_dict)

                tipo_despesas_values.append(tipo_despesa_dict)
                tipo_despesas_objs.append(tipo_despesa)

            fornecedor_values = {
                'nome': txtFornecedor,
                'cnpj_cpf': txtCNPJCPF
            }
            try:
                index = fornecedores_values.index(fornecedor_values)
                fornecedor = fornecedores_objs[index]
            except:
                fornecedor, _ = CotasParlamentaresFornecedor.objects \
                    .select_for_update() \
                    .get_or_create(**fornecedor_values)

                fornecedores_values.append(fornecedor_values)
                fornecedores_objs.append(fornecedor)

            passageiro_dict = {
                'nome': txtPassageiro
            }
            try:
                index = passageiros_values.index(passageiro_dict)
                passageiro = passageiros_objs[index]
            except:
                passageiro, _ = CotasParlamentaresPassageiro.objects \
                    .select_for_update() \
                    .get_or_create(**passageiro_dict)

                passageiros_values.append(passageiro_dict)
                passageiros_objs.append(passageiro)

            trecho_values = {
                'trecho': txtTrecho
            }

            try:
                index = trechos_values.index(trecho_values)
                trecho = trechos_objs[index]
            except:
                trecho, _ = CotasParlamentaresTrecho.objects \
                    .select_for_update() \
                    .get_or_create(**trecho_values)

                trechos_values.append(trecho_values)
                trechos_objs.append(trecho)

            if datEmissao:
                try:
                    datEmissao = parse(datEmissao)
                except:
                    datEmissao = None

            entry = {
                'task': task,
                'parlamentar': parlamentar,
                'partido': partido,
                'legislatura': legislatura,
                'unidade_federativa': unidade_federativa,
                'tipo_despesa': tipo_despesa,
                'fornecedor': fornecedor,

                # documento
                'numero_documento': txtNumero,
                'tipo_documento': indTipoDocumento,
                'parcela_documento': numParcela,
                'data_emissao': datEmissao,
                'valor_documento': vlrDocumento,
                'valor_glosa': vlrGlosa,
                'valor_liquido_documento': vlrLiquido,
                'id_documento': ideDocumento,
                'url_documento': urlDocumento,
                'mes_documento': numMes,
                'ano_documento': numAno,

                'passageiro': passageiro,
                'trecho': trecho,

                'numero_lote': numLote,
                'numero_ressarcimento': numRessarcimento,
                'valor_restituicao': vlrRestituicao,
                'identificar_solicitante': nuDeputadoId
            }

            batch.append(CotasParlamentares(**entry))

            if count == 100000:
                CotasParlamentares.objects.bulk_create(batch)
                batch = []
                count = 0
                gc.collect()
            else:
                count += 1

        CotasParlamentares.objects.bulk_create(batch)

        task.status = Task.COMPLETED

        gc.collect()

        return True
