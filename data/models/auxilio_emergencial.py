from django.db import models
from django.utils.translation import gettext as _


class AuxilioEmergencialUnidadeFederativa(models.Model):
    sigla = models.CharField(verbose_name='Sigla', max_length=2,
                             null=True, blank=True)

    def __str__(self):
        return self.sigla or '-'

    class Meta:
        verbose_name = _(u'Auxílio Emergêncial - Unidade Federativa')
        verbose_name_plural = _(u'Auxílio Emergêncial - Unidades Federativas')


class AuxilioEmergencialMunicipio(models.Model):
    codigo_municipio = models.PositiveIntegerField(
        verbose_name='CÓDIGO MUNICÍPIO', null=True, blank=True)

    nome_municipio = models.CharField(verbose_name='NOME MUNICÍPIO',
                                      max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.codigo_municipio} - {self.nome_municipio}'

    class Meta:
        verbose_name = _(u'Auxílio Emergêncial - Município')
        verbose_name_plural = _(u'Auxílio Emergêncial - Municípios')


class AuxilioEmergencialEnquadramento(models.Model):
    tipo = models.CharField(verbose_name='TIPO',
                            max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Auxílio Emergêncial - Enquadramento')
        verbose_name_plural = _(u'Auxílio Emergêncial - Enquadramentos')

    def __str__(self):
        return self.tipo or '-'


class AuxilioEmergencial(models.Model):
    task = models.ForeignKey('data.Task', verbose_name=_('Task'),
                             related_name='auxilio_emergencial',
                             on_delete=models.CASCADE)

    ano_disponibilizacao = models.PositiveIntegerField(
        verbose_name='ANO')

    mes_disponibilizacao = models.PositiveIntegerField(
        verbose_name='MÊS')

    unidade_federativa = models.ForeignKey(
        'data.AuxilioEmergencialUnidadeFederativa',
        verbose_name='Unidade Federativa',
        null=True, blank=True,
        on_delete=models.CASCADE)

    municipio = models.ForeignKey(
        'data.AuxilioEmergencialMunicipio',
        verbose_name='Município',
        null=True, blank=True,
        on_delete=models.CASCADE)

    nis_beneficiario = models.BigIntegerField(verbose_name='NIS BENEFICIÁRIO',
                                              null=True, blank=True)

    cpf_beneficiario = models.CharField(verbose_name='CPF BENEFICIÁRIO',
                                        max_length=20, null=True, blank=True)

    nome_beneficiario = models.CharField(verbose_name='NOME BENEFICIÁRIO',
                                         max_length=250, null=True, blank=True)

    nis_responsavel = models.BigIntegerField(verbose_name='NIS RESPONSÁVEL',
                                             null=True, blank=True)

    cpf_responsavel = models.CharField(verbose_name='CPF RESPONSÁVEL',
                                       max_length=20, null=True, blank=True)

    nome_responsavel = models.CharField(verbose_name='NOME RESPONSÁVEL',
                                        max_length=250, null=True, blank=True)

    enquadramento = models.ForeignKey(
        'data.AuxilioEmergencialEnquadramento',
        verbose_name='ENQUADRAMENTO',
        null=True, blank=True,
        on_delete=models.CASCADE)

    parcela = models.PositiveIntegerField(verbose_name='PARCELA',
                                          null=True, blank=True)

    observacao = models.TextField(verbose_name='OBSERVACAO',
                                  null=True,
                                  blank=True)

    valor_beneficio = models.FloatField(verbose_name='VALOR BENEFÍCIO')

    class Meta:
        ordering = ['id']
        verbose_name = _(u'Auxílio Emergêncial')
        verbose_name_plural = _(u'Auxílio Emergêncial')
