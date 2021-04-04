from django.db import models
from django.utils.translation import gettext as _


class AuxilioEmergencial(models.Model):
    task = models.ForeignKey('data.Task', verbose_name=_('Task'),
                             related_name='auxilio_emergencial',
                             on_delete=models.CASCADE)

    ano_disponibilizacao = models.PositiveIntegerField(
        verbose_name='ANO')

    mes_disponibilizacao = models.PositiveIntegerField(
        verbose_name='MÊS')

    uf = models.CharField(verbose_name='UF', max_length=2,
                          null=True, blank=True)

    codigo_municipio = models.PositiveIntegerField(
        verbose_name='CÓDIGO MUNICÍPIO', null=True, blank=True)

    nome_municipio = models.CharField(verbose_name='NOME MUNICÍPIO',
                                      max_length=255, null=True, blank=True)

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

    enquadramento = models.CharField(verbose_name='ENQUADRAMENTO',
                                     max_length=255, null=True, blank=True)

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
