from Backend.DataTypes.Document import Document
from Backend.DataTypes.Gender import Gender
from Backend.DataTypes.Form import Form
from Backend.DataTypes.Track import Track, TrackDetails
from Backend.DataTypes.Program import Program
from graphql.error import GraphQLError

class Applicant():
    def __init__(self, id, name, batch, track, email, consent, cv=None, scholarship=None, coverLetter=None, source=None, gender=None, acceptanceFormData=None, status="NEW", programDetails=None, generate=True):
        self.id = id
        self.name = name
        self.batch = batch
        self.track = TrackDetails(Track[track])
        self.email = email
        self.consent = consent
        self.coverLetter = Document(coverLetter, generate)
        self.cv = Document(cv, generate)
        self.scholarship = scholarship
        self.source = source
        self.gender = Gender.from_str(gender)
        self.acceptanceFormData = Form(acceptanceFormData)
        self.status = status
        self.program = Program(programDetails["id"],programDetails["short"], programDetails["title"], programDetails["logo"] )


    @classmethod
    def from_dict(cls, t):
        try:
            a = Applicant(t['id'],
                             t['name'],
                             t['batch'],
                             t['track'],
                             t['email'],
                             t['consent'],
                             t['cv'],
                             t['scholarship'],
                             t['coverLetter'],
                             t['gender'],
                             t['acceptanceFormData'],
                             t['status'],
                             t['programDetails'],
                             t['generate']
                             )
            return a
        except KeyError as err:
            raise GraphQLError(message="The field" + str(err) + "does not exists in the database document")

        


class PMCApplicant(Applicant):
    def __init__(self, id, name, batch, track, email, consent, cv, scholarship, coverLetter=None, source=None, gender=None, acceptanceFormData=None, project=None, strengths=None, status="NEW", programDetails=None):
        super().__init__(id, name, batch, track, email, consent, cv, scholarship,
                         coverLetter, source, gender, acceptanceFormData, status, programDetails)
        self.project = project
        self.strengths = strengths

