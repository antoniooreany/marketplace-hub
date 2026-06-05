import os
from dotenv import load_dotenv

_ = load_dotenv()

__all__ = ["Config", "TestingConfig"]

class Config:
    SECRET_KEY: str = os.environ.get('SECRET_KEY', 'dev-key-12345')
    SQLALCHEMY_DATABASE_URI: str = os.environ.get('DATABASE_URL', 'sqlite:///marketplace.db')
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False

class TestingConfig(Config):
    TESTING: bool = True
    SQLALCHEMY_DATABASE_URI: str = 'sqlite:///:memory:'
