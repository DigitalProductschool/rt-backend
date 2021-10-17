from Backend.database import db
from ariadne import MutationType
from ariadne import QueryType

batch_details = db.collection('batch-details')
batches = db.collection('batches')
users = db.collection('users')
mutation = MutationType()
query = QueryType()

def get_applicant_document(info, batch_id, applicant_id): 
    batch_doc = get_batch_doc(batch_id)
    applications = batch_doc.collection('applications')  
    application_doc = applications.document(str(applicant_id)) 
    if not application_doc.get().exists:
        raise Exception("Invalid applicant_id or there is no applicant with this Id in specified batch")
        
    application_details = application_doc.get().to_dict()
    return application_doc, application_details

def get_user_document(info, user_id): 
    user_doc = users.document(user_id)
    if not user_doc.get().exists:
        raise Exception("Invalid user_id") 
    user_details = user_doc.get().to_dict()
    return user_doc, user_details


def get_batch_doc(batch_id):
    batch_doc = batches.document('batch-' + str(batch_id))
    if not batch_doc.get().exists:
        raise Exception("Invalid Batch_id") 
    return batch_doc