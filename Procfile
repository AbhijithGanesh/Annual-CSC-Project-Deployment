python-3.9.2
web: gunicorn Django_Annual.wsgi --bind 0.0.0.0:$PORT
python manage.py collectstatic --noinput
manage.py makemigrations
manage.py migrate
