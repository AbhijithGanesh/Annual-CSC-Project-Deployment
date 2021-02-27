web: gunicorn Django_Annual.wsgi --log-file -
web: gunicorn Django_Annual.wsgi --bind 0.0.0.0:$PORT
manage.py migrate
manage.py makemigrations
manage.py migrate
