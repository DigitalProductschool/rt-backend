import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

class Config:
    SECRET_KEY = "hiringtool"
    TRELLO_API_KEY = os.environ.get("TRELLO_API_KEY")
    TRELLO_API_SECRET = os.environ.get("TRELLO_API_SECRET")
    TRELLO_BOARD_ID = os.environ.get("TRELLO_BOARD_ID")
    TRELLO_NAME = os.environ.get("TRELLO_NAME")
