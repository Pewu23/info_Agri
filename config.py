import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'info_farm89@#4()2'
