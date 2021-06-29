from datetime import timedelta
from google.cloud import secretmanager
from Backend.database import access_secret_version
import os

class Config:
    DEBUG = False
    DEVELOPMENT = False
    SECRET_KEY = "hiringtool"
    TRELLO_API_KEY = access_secret_version("trello-api-key")
    TRELLO_API_SECRET = access_secret_version("trello-api-secret")

class ProductionConfig(Config):
    TRELLO_BOARD_ID = access_secret_version("trello-board-id-se")
    TRELLO_NAME = access_secret_version("trello-board-name-se")


class StagingConfig(Config):
    DEBUG = True
    TRELLO_BOARD_ID = access_secret_version("trello-board-id-se-staging")
    TRELLO_NAME = access_secret_version("trello-board-name-se-staging")

class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True

configs = {
    'production': ProductionConfig,
    'staging': StagingConfig,
    'development': DevelopmentConfig,
}

env_config =  os.environ.get('FLASK_ENV', 'development')
config = configs[env_config]
