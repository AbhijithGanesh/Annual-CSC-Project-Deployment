web: gunicorn project.wsgi:application --log-file - --log-level debug
web: gunicorn project.wsgi:application --log-file=-
web: gunicorn hello:app
web: gunicorn --bind 0.0.0.0:8000 hello:app
python manage.py collectstatic --noinput
manage.py migrate
