import os
from datetime import timedelta
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """Base configuration"""
    user = os.environ["POSTGRES_USER"]
    password = os.environ["POSTGRES_PW"]
    hostname = os.environ["POSTGRES_HOST"]
    port = os.environ["POSTGRES_PORT"]
    database = os.environ["APPLICATION_DB"]

    DEBUG = False
    TESTING = False
    CSRF_FIELD = True
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+psycopg2://{user}:{password}@{hostname}:{port}/{database}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_POOL_SIZE = 1
    # SQLALCHEMY_MAX_OVERFLOW = 0
    SQLALCHEMY_ENGINE_OPTIONS = {
        "max_overflow": 15,
        "pool_pre_ping": True,
        "pool_recycle": 60 * 60,
        "pool_size": 30,
    }

    # JWT
    # JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)
    # JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    if os.environ['FLASK_CONFIG'] == 'production':
        SECRET_KEY = os.environ['SECRET_KEY']
        JWT_SECRET_KEY = os.environ["SECRET_KEY"]
        # S3 Bucket
        # S3_BUCKET = os.environ["S3_BUCKET"]
        # S3_KEY = os.environ["S3_KEY"]
        # S3_SECRET = os.environ["S3_SECRET"]

class DevelopmentConfig(Config):
    """Development configuration"""
    DEVELOPMENT = True
    DEBUG = True
    SECRET_KEY = 'development'
    JWT_SECRET_KEY = 'development'

class TestingConfig(Config):
    """Testing configuration"""

    TESTING = True
    DEBUG = True
    SECRET_KEY = 'development'
    JWT_SECRET_KEY = 'development'