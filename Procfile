web: gunicorn project.wsgi:application --log-file -

worker: python manage.py rqworker heroku
