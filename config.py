import os
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    DEBUG = os.environ.get("DEBUG")
    CSRF_ENABLED = os.environ.get("CSRF_ENABLED")
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get(
        "SQLALCHEMY_TRACK_MODIFICATIONS")


class DevelopmentConfig(Config):
    DEBUG = True
