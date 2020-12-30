"""
WSGI config for Django_Annual project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import sys
from Django_Annual import Password_Generator  as application
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_Annual.settings')

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
