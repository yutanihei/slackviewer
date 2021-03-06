"""
WSGI config for slackviewer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

# 一旦、WhiteNoiseを3.3.1に戻した

import os

from dj_static import Cling
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "slackviewer.settings")

application = Cling(get_wsgi_application())