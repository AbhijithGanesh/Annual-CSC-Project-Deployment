web: gunicorn Django_Annual.wsgi --log-file -
web: gunicorn Django_Annual.wsgi --bind 0.0.0.0:$PORT
python manage.py collectstatic 
manage.py migrate
manage.py makemigrations
manage.py migrate
