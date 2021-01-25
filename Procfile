
web: gunicorn Django_Annual.wsgi --bind 0.0.0.0:$PORT
python manage.py collectstatic --noinput
manage.py migrate
manage.py makemigrations
manage.py migrate
