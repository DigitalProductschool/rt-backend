from ariadne import MutationType
from ariadne import UnionType

from Backend.database import db
from Backend.DataTypes.Status import Status, StatusType
from Backend.DataTypes.User import User

from Backend.Authentication.verify_token import get_user_context
from Backend.DataTypes.AuthenticationException import AuthenticationException



batch_details = db.collection('batch-details')
batches = db.collection('batches')
mutation = MutationType()

coolnessThreshold = 3.5 # threshold that if exceeded changed an applicant status to PRETTY_COOL
requiredVotesNo = 2 # required number of votes for the threshold to be changed


@mutation.field("rate")
def resolve_rate(_, info, batch_id, applicant_id, score):
    current_user = get_user_context(info)
    # current_user = User(655525656,"Magda", "ntmagda93@gmail.com", "photo")
    if(current_user):
        applications = batches.document(
            'batch-' + str(batch_id)).collection('applications')
        applicant = applications.document(str(applicant_id))
        ratings = applicant.get().to_dict()['ratings']
        ratings[str(current_user.uid)] = score
        applicant.update({"ratings": ratings})

        if(len(ratings) > requiredVotesNo):
            filtered_vals = [v for _, v in ratings.items()]
            average = sum(filtered_vals) / len(filtered_vals)

            if average > coolnessThreshold:
                return Status(StatusType.PRETTY_COOL, "user voted succesfully")
            else:
                return Status(StatusType.NEUTRAL, "user voted succesfully")
        else:
            return  Status(StatusType.NEW, "user voted succesfully")
    else:
        return AuthenticationException(404, "User does not have permissions")


RateMutationResult = UnionType("RateMutationResult")
@RateMutationResult.type_resolver
def resolve_rate_mutatation_result(obj, *_):
    if isinstance(obj, Status):
        return "Status"
    if isinstance(obj, AuthenticationException):
        return "AuthenticationException"
    return None