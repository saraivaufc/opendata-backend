import hashlib
import os
import time
from functools import partial
from tempfile import NamedTemporaryFile, gettempdir

from celery import shared_task
from django.conf import settings

from data.models import Task
from data.services import get_service


@shared_task(queue='tasks')
def update_dataset(task_id):
    task = Task.objects.get(id=task_id)

    if settings.PRODUCTION:
        filename = os.path.basename(task.source.name)

        hash = hashlib.sha256()
        hash.update(str(time.time()).encode())
        time_hash = hash.hexdigest()[:10]
        dir_name = time_hash + "_" + filename.split('.')[0]
        dir = os.path.join(gettempdir(), dir_name)
        os.mkdir(dir)

        file = NamedTemporaryFile(delete=False, prefix="",
                                  suffix=filename, dir=dir)

        source_file = task.source.open()

        for chunk in iter(partial(source_file.read,
                                  settings.FILE_READ_CHUNK_SIZE), b''):
            file.write(chunk)
        file.close()
        file = file.name
    else:
        file = task.source.path

    task.status = Task.RUNNING
    task.save()

    service = get_service[task.dataset]

    if service.update_dataset(task, file):
        task.status = Task.COMPLETED
    else:
        task.status = Task.FAILED
        task.details = 'Aborted - an error has occurred.'
    task.save()

    if settings.PRODUCTION:
        try:
            os.remove(file)
        except Exception as e:
            task.status = Task.FAILED
            task.details = str(e)
            task.save()
