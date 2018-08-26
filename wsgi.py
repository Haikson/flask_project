from app import create_app
from werkzeug.contrib.fixers import ProxyFix

application = create_app(config_obj='app.config.ProductionConfig')
application.wsgi_app = ProxyFix(application.wsgi_app)
