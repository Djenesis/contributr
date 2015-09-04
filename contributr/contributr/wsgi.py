"""
WSGI config for contributr project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

if os.environ.get("DJANGO_SETTINGS_MODULE") == "contributr.settings.production":
    # Cling is a simple way of serving static assets.
    # http://www.kennethreitz.org/essays/introducing-dj-static
    from dj_static import Cling
    application = Cling(get_wsgi_application())
else:
    application = get_wsgi_application()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "contributr.settings.local")
