from django.db import models
from django.utils.translation import gettext as _


class CotasParlamentaresParlamentar(models.Model):
    txNomeParlamentar = models.CharField(verbose_name='txNomeParlamentar',
                                         max_length=255,
                                         null=True, blank=True)

    cpf = models.BigIntegerField(verbose_name='cpf',
                                 null=True, blank=True)

    ideCadastro = models.IntegerField(verbose_name='ideCadastro',
                                      null=True, blank=True)

    nuCarteiraParlamentar = models.IntegerField(
        verbose_name='nuCarteiraParlamentar',
        null=True, blank=True)

    def __str__(self):
        return self.txNomeParlamentar


class CotasParlamentaresPartido(models.Model):
    sgPartido = models.CharField(verbose_name='sgPartido', max_length=255,
                                 null=True, blank=True)

    def __str__(self):
        return self.sgPartido


class CotasParlamentaresTxtDescricao(models.Model):
    txtDescricao = models.CharField(verbose_name='txtDescricao',
                                    max_length=255,
                                    null=True, blank=True)

    def __str__(self):
        return self.txtDescricao


class CotasParlamentaresFornecedor(models.Model):
    txtFornecedor = models.CharField(verbose_name='txtFornecedor',
                                     max_length=255,
                                     null=True, blank=True)

    txtCNPJCPF = models.CharField(verbose_name='txtCNPJCPF',
                                  max_length=30, null=True, blank=True)

    def __str__(self):
        return self.txtFornecedor


class CotasParlamentaresPassageiro(models.Model):
    txtPassageiro = models.CharField(verbose_name='txtPassageiro',
                                     max_length=255, null=True, blank=True)

    def __str__(self):
        return self.txtPassageiro


class CotasParlamentaresTrecho(models.Model):
    txtTrecho = models.CharField(verbose_name='txtTrecho', max_length=255,
                                 null=True, blank=True)

    def __str__(self):
        return self.txtTrecho


class CotasParlamentares(models.Model):
    task = models.ForeignKey('data.Task', verbose_name=_('Task'),
                             related_name='cotas_parlamentares',
                             on_delete=models.CASCADE)

    parlamentar = models.ForeignKey('data.CotasParlamentaresParlamentar',
                                    verbose_name='Parlamentar',
                                    null=True, blank=True,
                                    on_delete=models.CASCADE)

    nuLegislatura = models.IntegerField(verbose_name='nuLegislatura',
                                        null=True, blank=True)

    sgUF = models.CharField(verbose_name='sgUF', max_length=2, null=True,
                            blank=True)

    partido = models.ForeignKey('data.CotasParlamentaresPartido',
                                verbose_name='Partido',
                                null=True, blank=True,
                                on_delete=models.CASCADE)

    codLegislatura = models.IntegerField(verbose_name='codLegislatura',
                                         null=True, blank=True)

    numSubCota = models.IntegerField(verbose_name='numSubCota',
                                     null=True, blank=True)

    txtDescricao = models.ForeignKey('data.CotasParlamentaresTxtDescricao',
                                     verbose_name='txtDescricao',
                                     null=True, blank=True,
                                     on_delete=models.CASCADE)

    numEspecificacaoSubCota = models.IntegerField(
        verbose_name='numEspecificacaoSubCota',
        null=True, blank=True)

    txtDescricaoEspecificacao = models.CharField(
        verbose_name='txtDescricaoEspecificacao',
        max_length=255, null=True, blank=True)

    fornecedor = models.ForeignKey('data.CotasParlamentaresFornecedor',
                                   verbose_name='Fornecedor',
                                   null=True, blank=True,
                                   on_delete=models.CASCADE)

    txtNumero = models.CharField(verbose_name='txtNumero',
                                 max_length=30, null=True, blank=True)

    indTipoDocumento = models.PositiveIntegerField(
        verbose_name='indTipoDocumento',
        null=True, blank=True)

    datEmissao = models.DateTimeField(verbose_name='datEmissao', null=True,
                                      blank=True)

    vlrDocumento = models.FloatField(verbose_name='vlrDocumento',
                                     null=True, blank=True)

    vlrGlosa = models.FloatField(verbose_name='vlrGlosa', null=True,
                                 blank=True)

    vlrLiquido = models.FloatField(verbose_name='vlrLiquido', null=True,
                                   blank=True)

    numMes = models.PositiveIntegerField(verbose_name='numMes', null=True,
                                         blank=True)

    numAno = models.PositiveIntegerField(verbose_name='numAno', null=True,
                                         blank=True)

    numParcela = models.PositiveIntegerField(verbose_name='numParcela',
                                             null=True, blank=True)

    passageiro = models.ForeignKey('data.CotasParlamentaresPassageiro',
                                   verbose_name='Passageiro',
                                   null=True, blank=True,
                                   on_delete=models.CASCADE)

    trecho = models.ForeignKey('data.CotasParlamentaresTrecho',
                               verbose_name='trecho',
                               null=True, blank=True,
                               on_delete=models.CASCADE)

    numLote = models.PositiveIntegerField(verbose_name='numLote', null=True,
                                          blank=True)

    numRessarcimento = models.PositiveIntegerField(
        verbose_name='numRessarcimento', null=True, blank=True)

    vlrRestituicao = models.FloatField(verbose_name='vlrRestituicao',
                                       null=True, blank=True)

    nuDeputadoId = models.PositiveIntegerField(verbose_name='nuDeputadoId',
                                               null=True, blank=True)

    ideDocumento = models.PositiveIntegerField(verbose_name='ideDocumento',
                                               null=True, blank=True)

    urlDocumento = models.URLField(verbose_name='urlDocumento',
                                   null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = _(u'Cota Parlamentar')
        verbose_name_plural = _(u'Cotas Parlamentares')
