from ariadne import MutationType
from ariadne import UnionType

from Backend.database import db
from Backend.DataTypes.Status import Status, StatusType
from Backend.DataTypes.User import User

from Backend.Authentication.verify_token import get_user_context
from Backend.DataTypes.Exceptions.AuthenticationException import AuthenticationException
from Backend.DataTypes.Exceptions.IncorrectParameterException import IncorrectParameterException



batch_details = db.collection('batch-details')
batches = db.collection('batches')
mutation = MutationType()

coolnessThreshold = 3.5 # threshold that if exceeded changed an applicant status to PRETTY_COOL
requiredVotesNo = 2 # required number of votes for the threshold to be changed


@mutation.field("rate")
def resolve_rate(_, info, batch_id, applicant_id, score):
    current_user = get_user_context(info)
    # current_user = User(1232499,"Magda", "ntmagda393@gmail.com", "photo")
    if(current_user):
        batch_doc = batches.document('batch-' + str(batch_id))
        if not batch_doc.get().exists:
            return IncorrectParameterException(errorMessage='Invalid batch_id')
            
        applications = batch_doc.collection('applications')        
        application = applications.document(str(applicant_id))

        if not application.get().exists:
            return IncorrectParameterException(errorMessage='Invalid applicant_id')

        application_details = application.get().to_dict()
        ratings = application_details['ratings']
        ratings[str(current_user.uid)] = score
        application.update({'ratings': ratings})
        return setApplicantStatus(ratings)
    else:
        return AuthenticationException()



def setApplicantStatus(ratings):
    if ( len(ratings) > requiredVotesNo ):
        filtered_vals = [v for _, v in ratings.items()]
        average = sum(filtered_vals) / len(filtered_vals)

        if average > coolnessThreshold:
            return Status(StatusType.PRETTY_COOL, "user voted succesfully")
        else:
            return Status(StatusType.NEUTRAL, "user voted succesfully")
    else:
        return  Status(StatusType.NEW, "user voted succesfully")



RateMutationResult = UnionType("RateMutationResult")
@RateMutationResult.type_resolver
def resolve_rate_mutatation_result(obj, *_):
    if isinstance(obj, Status):
        return "Status"
    if isinstance(obj, AuthenticationException):
        return "Exception"
    if isinstance(obj, IncorrectParameterException):
        return "Exception"
    return None

