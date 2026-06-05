import os
from typing import Final
from dotenv import load_dotenv

_ = load_dotenv()

__all__ = ["Config", "TestingConfig"]

class Config:
    SECRET_KEY: Final[str] = os.environ.get('SECRET_KEY', 'dev-key-12345')
    SQLALCHEMY_DATABASE_URI: Final[str] = os.environ.get('DATABASE_URL', 'sqlite:///marketplace.db')
    SQLALCHEMY_TRACK_MODIFICATIONS: Final[bool] = False

class TestingConfig(Config):
    TESTING: Final[bool] = True
    SQLALCHEMY_DATABASE_URI: Final[str] = 'sqlite:///:memory:'
