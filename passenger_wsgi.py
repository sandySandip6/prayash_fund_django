import sys
import os

# Path to your project root
sys.path.insert(0, os.path.dirname(__file__))

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'prayash_fund.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
