import os

basedir = os.environ.get("DB_PARENT_PATH", os.path.abspath(os.path.dirname(__file__)))
DATABASE_PATH = os.path.join(basedir, 'data.sqlite')


class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
    SQLALCHEMY_TRACK_MODIFICATIONS = False


logger_config = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '%(asctime)s :: %(levelname)s :: %(threadName)s :: %(module)s :: %(message)s',
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': "fichier_de_log.log",
            'formatter': 'default',
        },
    },
    'root': {
        'level': "INFO",
        'handlers': ['console', 'file']
    }
}