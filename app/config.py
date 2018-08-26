import os
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    """Base configuration."""
    FLASK_DEBUG = False
    SECRET_KEY = ';ajksd0jd0pqojdasdm[qpodsmq09d03jdlskmd03j1ldmlsad9jiodn;ajwd09j1ndla'  # todo generate secret key
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_POOL_SIZE = 5

    # EMAIL CONFIG
    EMAIL_BACKEND = 'flask_email.backends.smtp.Mail'
    DEFAULT_FROM_EMAIL = '{email}'
    DEFAULT_TO_EMAIL = ['kamo@haikson.com', 'info@techelec.ru']
    EMAIL_HOST = '{email_smtp_host}'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = '{email}'
    EMAIL_HOST_PASSWORD = '{password}'
    EMAIL_USE_TLS = False
    EMAIL_USE_SSL = False

    # administrator list
    ADMINS = ['kamo@haikson.com']


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    FLASK_DEBUG = True
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    WTF_CSRF_ENABLED = False
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(
    #     os.path.join(basedir, 'dev.db'))

    SQLALCHEMY_DATABASE_URI = '{database_engine}://{login}:{password}@{host}:{port}/{database}'
    DEBUG_TB_ENABLED = True


class TestingConfig(BaseConfig):
    """Testing configuration."""
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'
    DEBUG_TB_ENABLED = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(BaseConfig):
    """Production configuration."""
    SQLALCHEMY_DATABASE_URI = '{database_engine}://{login}:{password}@{host}:{port}/{database}'
    DEBUG_TB_ENABLED = False
