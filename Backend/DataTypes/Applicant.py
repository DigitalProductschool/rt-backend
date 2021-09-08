from Backend.DataTypes.Document import Document
from Backend.DataTypes.Gender import Gender
from Backend.DataTypes.Form import Form

class Applicant():
   def __init__(self, id, name, batch, track, email, consent, coverLetter, cv, scholarship, source, gender, acceptanceFormData, status="NEW"):
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
       self.acceptanceFormData = Form(acceptanceFormData)
       self.status  = status