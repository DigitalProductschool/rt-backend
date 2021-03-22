from ariadne import QueryType
from database import db
from DataTypes.Applicant import Applicant, Document

query = QueryType()


@query.field("applicants")
def resolve_applicants(_, info, batch_id):
    Applicants = []
    batches = db.collection('batches')
    applications = batches.document('batch-' + str(batch_id)).collection('applications')
    applications = [doc.to_dict() for doc in applications.stream()]

    for application in applications:
        applicant = Applicant(application['name'],
                              application['batch'],
                              application['track'],
                              application['email'],
                              application['consent'],
                              application['coverLetter'],
                              application['cv'],
                              application['scholarship'],
                              application['source']    
                              )
        Applicants.append(applicant)
    return Applicants
