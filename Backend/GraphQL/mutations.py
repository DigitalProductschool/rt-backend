from ariadne import MutationType
from Backend.database import db
from Backend.DataTypes.User import User
from Backend.Authentication.verify_token import get_user_context


batch_details = db.collection('batch-details')
batches = db.collection('batches')
mutation = MutationType()


@mutation.field("rate")
def resolve_rate(_, info, batch_id, applicant_id, score):
    current_user = get_user_context(info)
    # current_user = User(12345226755,"Magda", "ntmagda93@gmail.com", "photo")
    if(current_user):
        applications = batches.document(
            'batch-' + str(batch_id)).collection('applications')
        applicant = applications.document(str(applicant_id))
        ratings = applicant.get().to_dict()['ratings']
        ratings[str(current_user.uid)] = score
        applicant.update({"ratings": ratings})
        return True
    else:
        return False

