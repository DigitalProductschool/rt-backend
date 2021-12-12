from firebase_admin import storage
from datetime import timedelta
import datetime

class Document():

    def generate_url(self, name, bucketName):
         bucket = storage.bucket(bucketName)
         blob = bucket.blob(name)
         url = blob.generate_signed_url(datetime.timedelta(seconds=30), method='GET')
         return url

    def __init__(self, document):
        if type(document) == str:
            self.name = 'null'
            self.bucket = 'null'
            self.url = 'null'
        elif type(document) == dict:
            self.name = document['name']
            self.bucket = document['bucket']
            self.url = self.generate_url(document['name'], document['bucket'])
        else:
            return None