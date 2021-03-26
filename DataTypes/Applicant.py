import  enum 
# for now Track Enum is not used, because track is represetned as a string in the database - maybe we should change that?
class Track(enum.Enum):
    SE = 1
    AI = 2
    PM = 3
    UX = 4
    AC = 5
    PMC = 6

    @staticmethod
    def from_str(label):
        if label == 'se':
            return Track.SE
        if label == 'ai':
            return Track.AI
        if label == 'pm':
            return Track.PM
        if label == 'ixd':
            return Track.UX
        if label == 'ac':          
            return Track.AC
        if label == 'pmc':          
            return Track.PMC
        else:
            raise NotImplementedError


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

class Applicant():
   def __init__(self, name, batch, track, email, consent, coverLetter, cv, scholarship, source):
       self.name = name
       self.batch = batch
       self.track = Track.from_str(track)
       self.email = email
       self.consent = consent
       self.coverLetter = Document(coverLetter)
       self.cv = Document(cv)
       self.scholarship = scholarship
       self.source = source