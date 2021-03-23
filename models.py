from ariadne import QueryType, ScalarType
from database import db
from DataTypes.Applicant import Applicant, Document
from DataTypes.Batch import Batch

batch_details = db.collection('batch-details')
batches = db.collection('batches')
query = QueryType()

@query.field("applicants")
def resolve_applicants(_, info, batch_id):
    Applicants = []
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


@query.field("batches")
def resolve_batches(_, info, batch_id):
    Batches = []
    if batch_id:
        batch = batch_details.document(str(batch_id)).get().to_dict()
        # batch = Batch(**batch)
        batch = Batch(batch['batch'],
                      batch['startDate'],
                      batch['endDate'],
                      batch['appStartDate'],
                      batch['appEndDate'],
                      batch['appEndDate-ai'],
                      batch['appEndDate-ixd'],
                      batch['appEndDate-pm'],
                      batch['appEndDate-se']    
                     )
        Batches.append(batch)
        return Batches
    else:
        all_batches = [doc.to_dict() for doc in batch_details.stream()]
        for batch in all_batches:
            # batch = Batch(**batch)
            batch = Batch(batch['batch'],
                          batch['startDate'],
                          batch['endDate'],
                          batch['appStartDate'],
                          batch['appEndDate'],
                          batch['appEndDate-ai'],
                          batch['appEndDate-ixd'],
                          batch['appEndDate-pm'],
                          batch['appEndDate-se']
                         )               
            Batches.append(batch)
    return Batches