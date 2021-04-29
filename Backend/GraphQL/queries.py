from ariadne import QueryType
from Backend.database import db
from Backend.DataTypes.Applicant import Applicant
from Backend.DataTypes.Batch import Batch
from Backend.Authentication.auth_decorator import login_required

batch_details = db.collection('batch-details')
batches = db.collection('batches')
query = QueryType()


@query.field("applicants")
def resolve_applicants(_, info, batch_id):
    try:
        applicants = []
        applications = batches.document(
            'batch-' + str(batch_id)).collection('applications')
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
                                  application['source'],
                                  application['gender']
                                  )
            applicants.append(applicant)
        return applicants
    except:
        print("User does not have permissions")
        return None


@query.field("batches")
@login_required
def resolve_batches(_, info, batch_id):
    batches = []
    if batch_id:
        batch = batch_details.document(str(batch_id)).get().to_dict()
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
        batches.append(batch)
        return batches
    else:
        all_batches = [doc.to_dict() for doc in batch_details.stream()]
        for batch in all_batches:
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
            batches.append(batch)
    return batches
