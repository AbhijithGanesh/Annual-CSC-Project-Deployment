
web: gunicorn Password_Generator:app
gunicorn --bind 0.0.0.0:$PORT app:Password_Generator
python manage.py collectstatic --noinput
manage.py migrate
