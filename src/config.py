from os import path, environ

from dotenv import load_dotenv

"""Global App configuration"""

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '../.env'))

class Config:
    DB_HOST = environ.get("DB_HOST")
    DB_PORT = environ.get("DB_PORT")
    DB_NAME = environ.get("DB_NAME")
    DB_USER = environ.get("DB_USER")
    DB_PASS = environ.get("DB_PASS")

    SECRET = environ.get("SECRET")