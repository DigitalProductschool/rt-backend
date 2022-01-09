from datetime import timedelta
from google.cloud import secretmanager
from Backend.database import access_secret_version
import os

class Config:
    DEBUG = False
    DEVELOPMENT = False
    SECRET_KEY = "hiringtool"

class ProductionConfig(Config):
    ACCEPTANCE_FORM = "https://rt-frontend-production-w2a4py2tca-ey.a.run.app/form/"
    BUCKET_NAME = "dps-website-244212.appspot.com"

class StagingConfig(Config):
    DEBUG = True
    ACCEPTANCE_FORM = "https://rt-frontend-staging-w2a4py2tca-ey.a.run.app/form/"
    BUCKET_NAME = "dps-website-staging-0.appspot.com"

class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    ACCEPTANCE_FORM = "https://rt-frontend-staging-w2a4py2tca-ey.a.run.app/form/"
    BUCKET_NAME = "dps-website-staging-0.appspot.com"

configs = {
    'production': ProductionConfig,
    'staging': StagingConfig,
    'development': DevelopmentConfig,
}

env_config =  os.environ.get('FLASK_ENV', 'development')
config = configs[env_config]
