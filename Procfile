web: gunicorn --worker-class=gevent --worker-connections=6 codefest.wsgi
worker: celery worker --app=codefest.celery