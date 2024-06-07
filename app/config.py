

import os


class Config:
    SECRET_KEY = b'\xa0\xf7b\xc3sw9\x8by\x978:\x8e\xde\xcf\x13'
    INSTANCE_FOLDER_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'instance')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(INSTANCE_FOLDER_PATH, 'user.db')
    SQLALCHEMY_BINDS = {
        'movies': 'sqlite:///' + os.path.join(INSTANCE_FOLDER_PATH, 'movies.db')
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_URL_PATH = '/static'
    SERVER_NAME = 'localhost:5000'
    APPLICATION_ROOT = '/'
    PREFERRED_URL_SCHEME = 'http'
    UPLOAD_FOLDER = 'static/uploads'
    DEFAULT_PICS_FOLDER = 'static/images/defaults'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
