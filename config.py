import os

class Config():
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///blog.db"
    SECRET_KEY = 'Th1s1ss3cr3t'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY")

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///blog.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    pass

class TestingConfig(Config):
    TESTING = True