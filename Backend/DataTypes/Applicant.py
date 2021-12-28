from Backend.DataTypes.Document import Document
from Backend.DataTypes.Gender import Gender
from Backend.DataTypes.Form import Form
from Backend.DataTypes.Track import Track, TrackDetails
from Backend.DataTypes.Program import Program

class Applicant():
    def __init__(self, id, name, batch, track, email, consent, cv=None, scholarship=None, coverLetter=None, source=None, gender=None, acceptanceFormData=None, status="NEW", programDetails=None):
        self.id = id
        self.name = name
        self.batch = batch
        self.track = TrackDetails(Track[track])
        self.email = email
        self.consent = consent
        self.coverLetter = Document(coverLetter) if coverLetter is not None else None
        self.cv = Document(cv) if cv is not None else None
        self.scholarship = scholarship
        self.source = source
        self.gender = Gender.from_str(gender)
        self.acceptanceFormData = Form(acceptanceFormData)
        self.status = status
        self.program = Program(programDetails["id"],programDetails["short"], programDetails["title"], programDetails["logo"] )


class PMCApplicant(Applicant):
    def __init__(self, id, name, batch, track, email, consent, cv, scholarship, coverLetter=None, source=None, gender=None, acceptanceFormData=None, project=None, strengths=None, status="NEW", programDetails=None):
        super().__init__(id, name, batch, track, email, consent, cv, scholarship,
                         coverLetter, source, gender, acceptanceFormData, status, programDetails)
        self.project = project
        self.strengths = strengths
