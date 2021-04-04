mkdir -p  /var/log/opendata/

celery -A opendata worker --beat -l info -E --concurrency=5 -n opendata_tasks -Q tasks --scheduler django_celery_beat.schedulers:DatabaseScheduler -f /var/log/opendata/tasks.log &
