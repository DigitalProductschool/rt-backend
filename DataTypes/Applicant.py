from enum import Enum
# for now Track Enum is not used, because track is represetned as a string in the database - maybe we should change that?
class Track(Enum):
    SE = 1
    AI = 2
    PM = 3
    UX = 4
    AC = 5

class Document():
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class Applicant():
   def __init__(self, name, batch, track, email, consent, coverLetter, cv, scholarship, source):
       self.name = name
       self.batch = batch
       self.track = track
       self.email = email
       self.consent = consent
       self.coverLetter = coverLetter
       self.cv = Document(**cv)
       self.scholarship = scholarship
       self.source = source

