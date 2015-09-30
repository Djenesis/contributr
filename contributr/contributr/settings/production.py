
# This file contains settings for the Heroku production server

from .base import *

# Parse database configuration from $DATABASE_URL in heroku environment
import dj_database_url
DATABASES = {'default': dj_database_url.config()}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

DEBUG = True

# Allow https protocol to be used with callback urls in allauth
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"
