# project/server/__init__.py


import os

from flask import Flask, render_template, g
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_debugtoolbar import DebugToolbarExtension
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail


# instantiate the extensions
login_manager = LoginManager()
bcrypt = Bcrypt()
toolbar = DebugToolbarExtension()
bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate()
mail = Mail()


def create_app(script_info=None, config_obj='app.config.DevelopmentConfig'):

    # instantiate the app
    app = Flask(
        __name__,
        template_folder='../templates',
        static_folder='../static'
    )

    # set config
    app_settings = os.getenv(
        'APP_SETTINGS', config_obj)
    app.config.from_object(app_settings)

    # set up extensions
    login_manager.init_app(app)
    bcrypt.init_app(app)
    toolbar.init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    # register blueprints
    register_blueprints(app)

    # flask login
    from user.models import User
    login_manager.login_view = 'user.login'
    login_manager.login_message_category = 'danger'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.filter(User.id == int(user_id)).first()

        return app

    @app.before_request
    def before_request():
        from content.models import News
        g.sidebar_news = News.query.order_by(News.date.desc()).limit(5).all()
        return

    # error handlers
    @app.errorhandler(401)
    def unauthorized_page(error):
        return render_template('errors/401.html'), 401

    @app.errorhandler(403)
    def forbidden_page(error):
        return render_template('errors/403.html'), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def server_error_page(error):
        return render_template('errors/500.html'), 500

    # shell context for flask cli
    app.shell_context_processor({'app': app, 'db': db})

    return app


def register_blueprints(app):
    from content.views import content_blueprint
    from news.views import news_blueprint
    from user.views import user_blueprint
    from app.views.feedback import feedback_blueprint

    from app.views.admin import admin_blueprint

    app.register_blueprint(user_blueprint)
    app.register_blueprint(content_blueprint)
    app.register_blueprint(news_blueprint)
    app.register_blueprint(feedback_blueprint)
    app.register_blueprint(admin_blueprint)
