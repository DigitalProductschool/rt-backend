from Backend.DataTypes.Document import Document
from Backend.DataTypes.Gender import Gender
from Backend.DataTypes.Form import Form
from Backend.DataTypes.Track import Track, TrackDetails
from Backend.DataTypes.Program import Program

class Applicant():
    def __init__(self, id, name, batch, track, email, consent, cv, scholarship, coverLetter=None, source=None, gender=None, acceptanceFormData=None, status="NEW", programDetails=None):
        self.id = id
        self.name = name
        self.batch = batch
        self.track = TrackDetails(Track[track])
        self.email = email
        self.consent = consent
        self.coverLetter = Document(coverLetter)
        self.cv = Document(cv)
        self.scholarship = scholarship
        self.source = source
        self.gender = Gender.from_str(gender)
        self.acceptanceFormData = Form(acceptanceFormData)
        self.status = status
        self.program = Program(programDetails["id"],programDetails["short"], programDetails["title"] )


class PMCApplicant(Applicant):
    def __init__(self, id, name, batch, track, email, consent, cv, scholarship, coverLetter=None, source=None, gender=None, acceptanceFormData=None, project=None, strengths=None, status="NEW", programDetails=None):
        super().__init__(id, name, batch, track, email, consent, cv, scholarship,
                         coverLetter, source, gender, acceptanceFormData, status, program)
        self.project = project
        self.strengths = strengths
