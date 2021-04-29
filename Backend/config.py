import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

class Config:
    SECRET_KEY = "hiringtool"
    GOOGLE_CLIENT_ID = "633665395645-hdeb1r2j1cfo56fkm3o6ns8tb768c998.apps.googleusercontent.com"
    GOOGLE_CLIENT_SECRET = "ulpOcCaHBB-B7HUcim_LZ0ee"
    SESSION_COOKIE_NAME = 'google-login-session'
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=5)
