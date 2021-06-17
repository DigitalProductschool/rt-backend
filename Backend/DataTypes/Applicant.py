from Backend.DataTypes.Document import Document
from Backend.DataTypes.Gender import Gender

class Applicant():
   def __init__(self, id, name, batch, track, email, consent, coverLetter, cv, scholarship, source, gender, status="NEW"):
       self.id = id
       self.name = name
       self.batch = batch
       self.track = track
       self.email = email
       self.consent = consent
       self.coverLetter = Document(coverLetter)
       self.cv = Document(cv)
       self.scholarship = scholarship
       self.source = source
       self.gender = Gender.from_str(gender)
       self.status  = status