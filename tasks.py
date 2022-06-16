from celery import Celery
from celery.schedules import crontab

from webapp import create_app
from webapp.news.parsers import habr

flask_app = create_app()
celery_app = Celery('tasks', broker='redis://localhost:6379/0')

@celery_app.task
def habr_snippets():
    with flask_app.app_context():
        habr.get_news_snippets()

@celery_app.task
def habr_content():
    with flask_app.app_context():
        habr.get_news_content()

@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(minute='*/1'), habr_snippets.s())
    sender.add_periodic_task(crontab(minute='*/2'), habr_content.s())




""" Запустим Celery

Linux/Mac celery -A tasks worker --loglevel=info

Windows set FORKED_BY_MULTIPROCESSING=1 && celery -A tasks worker --loglevel=info 



Запустим celery-beat

Чтобы запуск задач по расписанию работал, мы должны запустить celery-beat. Именно он будет следить за расписанием и отправлять задачи worker-ам. 
Beat нужно запускать отдельно, поэтому понадобится еще одно окно терминала

celery -A tasks beat

Есть и более простой вариант, который можно использовать на очень маленьких проектах

celery -A tasks worker -B --loglevel=INFO

"""