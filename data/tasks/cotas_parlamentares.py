# import os
#
# import pytz
# from celery import shared_task
# from django.conf import settings
# from django.core.files import File
# from django.utils import timezone
# from django.utils.translation import gettext as _
#
# from data.models import Task
# from data.services.file import FileService
# from .dataset import update_dataset
#
#
# @shared_task(queue='task')
# def cotas_parlamentares_online():
#     file_service = FileService()
#
#     try:
#         remote_file = 'http://siscom.ibama.gov.br/shpsiscom/adm_embargo_a.zip'
#
#         provider_date = file_service.get_remote_file_last_mod_date(remote_file)
#         source_date = timezone.now() \
#             .astimezone(pytz.timezone(settings.TIME_ZONE))
#
#         if provider_date:
#             embargos_ibama_processing_today = LayerTask.objects.filter(
#                 dataset=LayerTask.EMBARGOS_IBAMA,
#                 source_date__date=source_date.date(),
#                 status__in=[LayerTask.READY, LayerTask.RUNNING]
#             )
#
#             embargos_ibama_completted_today = LayerTask.objects.filter(
#                 dataset=LayerTask.EMBARGOS_IBAMA,
#                 provider_date__gte=provider_date,
#                 status=LayerTask.COMPLETED
#             )
#
#             if not embargos_ibama_processing_today.exists() and \
#                     not embargos_ibama_completted_today.exists():
#
#                 file_path = file_service.download_file(remote_file,
#                                                        'adm_embargo_a.zip')
#
#                 reopen = File(open(file_path, 'rb'))
#
#                 basename = os.path.basename(file_path)
#                 filename, file_extension = os.path.splitext(basename)
#
#                 source_date_str = source_date.strftime('%Y-%m-%d_%H%M%S')
#
#                 new_filename = f'{filename}_{source_date_str}.{file_extension}'
#
#                 task = Task.objects.create(
#                     dataset=Task.EMBARGOS_IBAMA,
#                     source_format=Task.ZIP,
#                     source_date=source_date,
#                     provider_date=provider_date)
#
#                 task.source.save(new_filename, reopen)
#                 update_dataset(task.id)
#
#                 try:
#                     os.remove(file_path)
#                 except FileNotFoundError:
#                     pass
#
#         else:
#             raise Exception(_('Remote file has an invalid name.'))
#     except Exception as e:
#         LayerTask.objects.create(
#             dataset=LayerTask.EMBARGOS_IBAMA,
#             details=str(e),
#             status=LayerTask.FAILED
#         )
