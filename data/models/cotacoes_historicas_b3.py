from django.db import models
from django.utils.translation import gettext as _


class CotacoesHistoricasB3(models.Model):
    tipreg = models.IntegerField(verbose_name=_('TIPO DE REGISTRO'))

    datpre = models.DateField(verbose_name=_('DATA DO PREGÃO'))

    codbdi = models.IntegerField(verbose_name=_('CÓDIGO BDI'))

    codneg = models.CharField(verbose_name=_('CÓDIGO DE NEGOCIAÇÃO DO PAPEL'),
                              max_length=12)

    tpmerc = models.IntegerField(verbose_name=_('TIPO DE MERCADO'))

    nomres = models.CharField(
        verbose_name=_('NOME RESUMIDO DA EMPRESA EMISSORA DO PAPEL'),
        max_length=12, null=True, blank=True)

    especi = models.CharField(verbose_name=_('ESPECIFICAÇÃO DO PAPEL'),
                              max_length=10)

    prazot = models.IntegerField(
        verbose_name=_('PRAZO EM DIAS DO MERCADO A TERMO'), null=True)

    modref = models.CharField(verbose_name=_('MOEDA DE REFERÊNCIA'),
                              max_length=4)

    preabe = models.FloatField(verbose_name=_('PREÇO DE ABERTURA  DO PAPEL'))

    premax = models.FloatField(verbose_name=_('PREÇO DE MÁXIMO  DO PAPEL'))

    premin = models.FloatField(verbose_name=_('PREÇO MÍNIMO  DO PAPEL'))

    premed = models.FloatField(verbose_name=_('PREÇO MÉDIO DO PAPEL'))

    preult = models.FloatField(
        verbose_name=_('PREÇO DO ÚLTIMO NEGÓCIO DO PAPEL-MERCADO NO PREGÃO'))

    preofc = models.FloatField(
        verbose_name=_('PREÇO DA MELHOR OFERTA DE COMPRA'))

    preofv = models.FloatField(
        verbose_name=_('PREÇO DA MELHOR OFERTA DE VENDA'))

    totneg = models.CharField(
        verbose_name=_('NEG. NÚMERO DE NEGÓCIOS EFETUADOS COM O PAPEL'),
        max_length=5)

    quatot = models.BigIntegerField(
        verbose_name=_('QUANTIDADE TOTAL DE TÍTULOS NEGOCIADOS NESTE PAPEL'))

    voltot = models.BigIntegerField(
        verbose_name=_('VOLUME TOTAL DE TÍTULOS NEGOCIADOS NESTE PAPEL'))

    preexe = models.BigIntegerField(
        verbose_name=_('PREÇO DE EXERCÍCIOS PARA O MERCADO DE OPÇÕES'))

    indopc = models.IntegerField(
        verbose_name=_('INDICADOR DE CORREÇÃO DE PREÇOS'))

    datven = models.DateField(
        verbose_name=_('DATA DO VENCIMENTO PARA OS MERCADOS'))

    fatcot = models.BigIntegerField(verbose_name=_('FATOR DE COTAÇÃO DO PAPEL'))

    ptoexe = models.BigIntegerField(
        verbose_name=_('PREÇO DE EXERCÍCIO EM PONTOS PARA OPÇÕES REFERENCIADAS'
                       ' EM DÓLAR OU VALOR DE CONTRATO EM PONTOS PARA TERMO'
                       ' SECUNDÁRIO'))

    codisi = models.CharField(
        verbose_name=_('CÓDIGO DO PAPEL NO SISTEMA ISIN OU CÓDIGO INTERNO '
                       'DO PAPEL'), max_length=1)

    dismes = models.IntegerField(
        verbose_name=_('NÚMERO DE DISTRIBUIÇÃO DO PAPEL'))

    class Meta:
        verbose_name = _(u'Cotações Históricas - B3')
        verbose_name_plural = _(u'Cotações Históricas - B3')
