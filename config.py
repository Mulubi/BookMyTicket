import os
from os import getenv


# basedir = os.path.abspath(os.path.dirname(__file__))



class Config:
    SECRET_KEY = '41ed75074dc9acfc44d3ca8ab3d6477f'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    #SQLALCHEMY_DATABASE_URI = "mysql://bmt_dev:bmt_dev_pwd2023!@localhost/bmt_dev_db"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    # 'SQLALCHEMY_DATABASE_URI' = 'sqlite:///' + os.path.join(basedir, 'site.db')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
