web: gunicorn --worker-class=gevent --worker-connections=6 --workers=2 codefest.wsgi
worker: celery worker --app=codefest.celery