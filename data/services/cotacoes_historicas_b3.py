import gc
from datetime import datetime

from django.db import transaction
from tqdm import tqdm

from data.models import CotacoesHistoricasB3, Task
from data.services.file import FileService


class CotacoesHistoricasB3Service:
    def __init__(self):
        self.__file_service = FileService()

    @transaction.atomic
    def update_dataset(self, task, file_path):
        entries = self.__file_service.read_csv(file_path=file_path,
                                               sep=',',
                                               decimal='.',
                                               encoding='latin1',
                                               iterate=True)

        batch = []

        count = 0

        for data in tqdm(entries, miniters=100000):
            datpre = data.get('datpre')
            datven = data.get('datven')

            if datpre:
                datpre = datetime.strptime(datpre, '%Y-%m-%d')

            if datven:
                datven = datetime.strptime(datven, '%Y-%m-%d')

            entry = {
                'tipreg': data.get('tipreg'),
                'datpre': datpre,
                'codbdi': data.get('codbdi'),
                'codneg': data.get('codneg'),
                'tpmerc': data.get('tpmerc'),
                'nomres': data.get('nomres'),
                'especi': data.get('especi'),
                'prazot': data.get('prazot'),
                'modref': data.get('modref'),
                'preabe': data.get('preabe'),
                'premax': data.get('premax'),
                'premin': data.get('premin'),
                'premed': data.get('premed'),
                'preult': data.get('preult'),
                'preofc': data.get('preofc'),
                'preofv': data.get('preofv'),
                'totneg': data.get('totneg'),
                'quatot': data.get('quatot'),
                'voltot': data.get('voltot'),
                'preexe': data.get('preexe'),
                'indopc': data.get('indopc'),
                'datven': datven,
                'fatcot': data.get('fatcot'),
                'ptoexe': data.get('ptoexe'),
                'codisi': data.get('codisi'),
                'dismes': data.get('dismes')
            }

            batch.append(CotacoesHistoricasB3(**entry))

            if count == 100000:
                CotacoesHistoricasB3.objects.bulk_create(batch)
                batch = []
                count = 0
                gc.collect()
            else:
                count += 1

        CotacoesHistoricasB3.objects.bulk_create(batch)

        task.status = Task.COMPLETED

        gc.collect()

        return True
