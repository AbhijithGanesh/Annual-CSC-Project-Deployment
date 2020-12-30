
web: gunicorn --bind 0.0.0.0:$PORT hello:app
python manage.py collectstatic --noinput
manage.py migrate
