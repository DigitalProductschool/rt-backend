from datetime import timedelta
from google.cloud import secretmanager
from Backend.database import access_secret_version


class Config:
    SECRET_KEY = "hiringtool"
    TRELLO_API_KEY = access_secret_version("trello-api-key")
    TRELLO_API_SECRET = access_secret_version("trello-api-secret")
    TRELLO_BOARD_ID = access_secret_version("trello-board-id-se")
    TRELLO_NAME = access_secret_version("trello-board-name-se")
