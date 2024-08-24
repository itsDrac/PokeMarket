import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or "you'll never know"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
        "sqlite:///debug.db"
    ADMINS = ['gpt.sahaj28@gmail.com']


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True
    WTF_CSRF_ENABLED = False
