from django.db import models
from django.utils.translation import gettext as _


class CotasParlamentaresParlamentar(models.Model):
    nome = models.CharField(verbose_name='Nome do Parlamentar',
                            max_length=255,
                            null=True, blank=True)

    cpf = models.BigIntegerField(verbose_name='CPF do Parlamentar',
                                 null=True, blank=True)

    id_cadastro = models.IntegerField(
        verbose_name='Identificador Único do Parlamentar',
        null=True, blank=True)

    numero_carteira_parlamentar = models.IntegerField(
        verbose_name='Número da Carteira Parlamentar',
        null=True, blank=True)

    def __str__(self):
        return self.nome or '-'

    class Meta:
        ordering = ['nome']
        verbose_name = _(u'Cota Parlamentar - Parlamentar')
        verbose_name_plural = _(u'Cotas Parlamentares - Parlamentares')


class CotasParlamentaresPartido(models.Model):
    sigla = models.CharField(verbose_name='SIGLA', max_length=255,
                             null=True, blank=True)

    def __str__(self):
        return self.sigla or '-'

    class Meta:
        verbose_name = _(u'Cota Parlamentar - Partido')
        verbose_name_plural = _(u'Cotas Parlamentares - Partidos')


class CotasParlamentaresTipoDespesa(models.Model):
    numero = models.IntegerField(verbose_name='Número',
                                 null=True, blank=True)


    descricao = models.CharField(verbose_name='Descrição',
                                 max_length=255,
                                 null=True, blank=True)

    numero_especificacao = models.IntegerField(
        verbose_name='Número da Especificação',
        null=True, blank=True)

    descricao_especificacao = models.CharField(
        verbose_name='Descrição da Especificaçã',
        max_length=255, null=True, blank=True)

    def __str__(self):
        return self.descricao or '-'

    class Meta:
        verbose_name = _(u'Cota Parlamentar - Tipo de Despesa')
        verbose_name_plural = _(u'Cotas Parlamentares - Tipo de Despesa')


class CotasParlamentaresFornecedor(models.Model):
    nome = models.CharField(verbose_name='Nome',
                            max_length=255,
                            null=True, blank=True)

    cnpj_cpf = models.CharField(verbose_name='CNPJ/CPF',
                                max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nome or '-'

    class Meta:
        verbose_name = _(u'Cota Parlamentar - Fornecedor')
        verbose_name_plural = _(u'Cotas Parlamentares - Fornecedores')


class CotasParlamentaresPassageiro(models.Model):
    nome = models.CharField(verbose_name='Nome',
                            max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nome or '-'

    class Meta:
        verbose_name = _(u'Cota Parlamentar - Passageiro')
        verbose_name_plural = _(u'Cotas Parlamentares - Passageiros')


class CotasParlamentaresTrecho(models.Model):
    trecho = models.CharField(verbose_name='Trecho', max_length=255,
                              null=True, blank=True)

    def __str__(self):
        return self.trecho or '-'

    class Meta:
        verbose_name = _(u'Cota Parlamentar - Trecho')
        verbose_name_plural = _(u'Cotas Parlamentares - Trechos')

class CotasParlamentaresLegislatura(models.Model):
    numero = models.IntegerField(verbose_name='Número',
                                 null=True, blank=True)


    codigo = models.IntegerField(verbose_name='Código',
                                         null=True, blank=True)

    def __str__(self):
        return str(self.numero) or '-'

    class Meta:
        verbose_name = _(u'Cota Parlamentar - Legislatura')
        verbose_name_plural = _(u'Cotas Parlamentares - Legislaturas')

class CotasParlamentaresUnidadeFederativa(models.Model):
    sigla = models.CharField(verbose_name='Sigla', max_length=2, null=True,
                          blank=True)

    def __str__(self):
        return self.sigla or '-'

    class Meta:
        verbose_name = _(u'Cota Parlamentar - Unidade Federativa')
        verbose_name_plural = _(u'Cotas Parlamentares - Unidades Federativas')


class CotasParlamentares(models.Model):
    NOTA_FISCAL = 0
    RECIBO = 1
    DESPESA_NO_EXTERIOR = 2
    TIPO_DOCUMENTO_CHOICES = (
        (NOTA_FISCAL, 'Nota Fiscal'),
        (RECIBO, 'Recibo'),
        (DESPESA_NO_EXTERIOR, 'Despesa no Exterior'),
    )
    task = models.ForeignKey('data.Task', verbose_name=_('Task'),
                             related_name='cotas_parlamentares',
                             on_delete=models.CASCADE)

    parlamentar = models.ForeignKey('data.CotasParlamentaresParlamentar',
                                    verbose_name='Parlamentar',
                                    null=True, blank=True,
                                    on_delete=models.CASCADE)

    partido = models.ForeignKey('data.CotasParlamentaresPartido',
                                verbose_name='Partido',
                                null=True, blank=True,
                                on_delete=models.CASCADE)

    legislatura = models.ForeignKey('data.CotasParlamentaresLegislatura',
                                verbose_name='Legislatura',
                                null=True, blank=True,
                                on_delete=models.CASCADE)

    tipo_despesa = models.ForeignKey('data.CotasParlamentaresTipoDespesa',
                                     verbose_name='Tipo de Despesa',
                                     null=True, blank=True,
                                     on_delete=models.CASCADE)

    fornecedor = models.ForeignKey('data.CotasParlamentaresFornecedor',
                                   verbose_name='Fornecedor',
                                   null=True, blank=True,
                                   on_delete=models.CASCADE)

    unidade_federativa = models.ForeignKey('data.CotasParlamentaresUnidadeFederativa',
                                   verbose_name='Unidade Federativa',
                                   null=True, blank=True,
                                   on_delete=models.CASCADE)

    numero_documento = models.CharField(verbose_name='Número do Documeto',
                                        max_length=255, null=True, blank=True)

    tipo_documento = models.PositiveIntegerField(
        verbose_name='Tipo do Documento',
        choices=TIPO_DOCUMENTO_CHOICES,
        null=True, blank=True)

    parcela_documento = models.PositiveIntegerField(
        verbose_name='Número da Parcela do Documento', null=True, blank=True)

    data_emissao = models.DateTimeField(
        verbose_name='Data de Emissão do Documento', null=True, blank=True)


    valor_documento = models.FloatField(verbose_name='Valor do Documento',
                                        null=True, blank=True)

    valor_glosa = models.FloatField(verbose_name='vlrGlosa', null=True,
                                    blank=True)

    valor_liquido_documento = models.FloatField(
        verbose_name='Valor Líquido do Documento', null=True, blank=True)


    id_documento = models.PositiveIntegerField(verbose_name='Id do Documento',
                                               null=True, blank=True)

    url_documento = models.URLField(verbose_name='URL do Documento',
                                    null=True, blank=True)


    mes_documento = models.PositiveIntegerField(
        verbose_name='Mês do Documento', null=True, blank=True)

    ano_documento = models.PositiveIntegerField(
        verbose_name='Ano do Documento', null=True, blank=True)


    passageiro = models.ForeignKey('data.CotasParlamentaresPassageiro',
                                   verbose_name='Passageiro',
                                   null=True, blank=True,
                                   on_delete=models.CASCADE)

    trecho = models.ForeignKey('data.CotasParlamentaresTrecho',
                               verbose_name='trecho',
                               null=True, blank=True,
                               on_delete=models.CASCADE)

    numero_lote = models.PositiveIntegerField(verbose_name='Número do Lote',
                                              null=True, blank=True)

    numero_ressarcimento = models.PositiveIntegerField(
        verbose_name='Número do Ressarcimento', null=True, blank=True)

    valor_restituicao = models.FloatField(verbose_name='Valor da Restituição',
                                          null=True, blank=True)

    identificar_solicitante = models.PositiveIntegerField(
        verbose_name='Identificador do Solicitante', null=True, blank=True)

    class Meta:
        ordering = ['-data_emissao']
        verbose_name = _(u'Cota Parlamentar - Cota')
        verbose_name_plural = _(u'Cotas Parlamentares - Cotas')
