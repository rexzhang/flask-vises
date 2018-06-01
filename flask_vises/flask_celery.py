#!/usr/bin/env python
# coding=utf-8


from celery import Celery


def create_celery(name='flask'):
    return Celery(name)


def configure_celery(app, celery):
    # set broker url and result backend from app config
    celery.conf.broker_url = app.config['CELERY_BROKER_URL']
    celery.conf.result_backend = app.config['CELERY_RESULT_BACKEND']
    celery.conf.timezone = app.config['CELERY_TIMEZONE']
    celery.conf.task_send_sent_event = app.config['CELERY_TASK_SEND_SENT_EVENT']

    # subclass task base for app context
    # http://flask.pocoo.org/docs/dev/patterns/celery/
    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask

    # run finalize to process decorated tasks
    # celery.finalize()  # something wrong!
    return celery
