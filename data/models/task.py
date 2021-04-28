import os

from django.contrib.gis.db import models
from django.utils import timezone
from django.utils.translation import gettext as _

from data.storage_backends import PrivateMediaStorage


def get_file_path(instance, filename):
    creation_date = timezone.now().strftime("%Y%m%d%H%M%S")
    filename, file_extension = os.path.splitext(filename)
    new_filename = f'{filename}_{creation_date}{file_extension}'
    return os.path.join('LAYERS', instance.dataset, new_filename)


class Task(models.Model):
    AUXILIO_EMERGENCIAL = 'AUXILIO_EMERGENCIAL'
    COTAS_PARLAMENTARES = 'COTAS_PARLAMENTARES'
    COTACOES_HISTORICAS_B3 = 'COTACOES_HISTORICAS_B3'

    DATASET_CHOICES = (
        (AUXILIO_EMERGENCIAL, _('Auxílio Emergêncial')),
        (COTAS_PARLAMENTARES, _('Cotas Parlamentares')),
        (COTACOES_HISTORICAS_B3, _('Cotações Históricas B3')),
    )

    READY = 'READY'
    RUNNING = 'RUNNING'
    COMPLETED = 'COMPLETED'
    FAILED = 'FAILED'
    CANCELLED = 'CANCELLED'

    STATUS_CHOICES = (
        (READY, _('Ready')),
        (RUNNING, _('Running')),
        (COMPLETED, _('Completed')),
        (FAILED, _('Failed')),
        (CANCELLED, _('Cancelled')),
    )

    CSV = 'CSV'
    GPKG = 'GPKG'
    ZIP = 'ZIP'
    RAR = 'RAR'

    FORMAT_CHOICES = (
        (CSV, _('CSV')),
        (GPKG, _('GPKG')),
        (ZIP, _('ZIP')),
        (RAR, _('RAR'))
    )

    dataset = models.CharField(verbose_name=_('Dataset'),
                               choices=DATASET_CHOICES,
                               max_length=40)

    source = models.FileField(verbose_name=_('Source'),
                              storage=PrivateMediaStorage(),
                              upload_to=get_file_path,
                              null=True,
                              blank=True)

    source_date = models.DateTimeField(verbose_name=_('Source date'),
                                       null=True,
                                       blank=True)

    source_format = models.CharField(verbose_name=_('Source format'),
                                     max_length=20,
                                     choices=FORMAT_CHOICES,
                                     null=True,
                                     blank=True)

    status = models.CharField(verbose_name=_('Status'),
                              choices=STATUS_CHOICES,
                              max_length=40,
                              default=READY)

    details = models.TextField(verbose_name=_('Details'),
                               null=True,
                               blank=True)

    creation_date = models.DateTimeField(verbose_name=_('Creation date'),
                                         auto_now_add=True,
                                         editable=False)

    last_modification_date = models.DateTimeField(
        verbose_name=_('Last modification date'),
        auto_now=True)

    def __str__(self):
        return f'{self.source_date}'

    class Meta:
        ordering = ['-creation_date']
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')
        indexes = [
            models.Index(fields=['dataset']),
            models.Index(fields=['source_date']),
            models.Index(fields=['status'])
        ]
