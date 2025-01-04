import os

class ProductionConfig:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-production-secret-key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://myuser:mypassword@localhost:5432/mydatabase')

class DevelopmentConfig:
    DEBUG = True
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-production-secret-key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://myuser:mypassword@localhost:5432/mydatabase')

class TestConfig:
    DEBUG = True
    TESTING = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-production-secret-key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://myuser:mypassword@localhost:5432/mydatabase')
