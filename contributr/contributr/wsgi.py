"""
WSGI config for contributr project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "contributr.settings.local")

# Cling is a simple way of serving static assets.
# http://www.kennethreitz.org/essays/introducing-dj-static
application = Cling(get_wsgi_application())
