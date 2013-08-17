import sae
from uchange import wsgi

application = sae.create_wsgi_app(wsgi.application)