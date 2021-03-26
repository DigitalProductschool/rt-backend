class Document():
    def __init__(self, document):
        if type(document) == str:
            self.name = 'null'
            self.bucket = 'null'
        elif type(document) == dict:
            self.name = document['name']
            self.bucket = document['bucket']
        else:
            return None
