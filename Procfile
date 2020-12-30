
web: gunicorn Password_Generator:app
web: gunicorn --bind 0.0.0.0:8000 -a Password_Generator
python manage.py collectstatic --noinput
manage.py migrate
