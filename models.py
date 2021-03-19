from ariadne import QueryType
from database import db
from DataTypes.Applicant import Applicant

details_ref = db.collection('batch-details')
query = QueryType()
Applicants = []


@query.field("applicants")
def resolve_applicants(_, info):
    batches = db.collection('batches')
    batch_id = 11
    applications = batches.document('batch-'+str(batch_id)).collection('applications')
    participants_details = [doc.to_dict() for doc in applications.stream()]

    for applicant in participants_details:
        participant = Applicant(applicant['name'], applicant['batch'], applicant['email'])
        Applicants.append(participant)
    return Applicants