
from ariadne import UnionType
from Backend.DataTypes.Exceptions.IncorrectParameterException import IncorrectParameterException
from Backend.DataTypes.Exceptions.AuthenticationException import AuthenticationException
from Backend.DataTypes.Applicant import Applicant
from Backend.DataTypes.ApplicantList import ApplicantList
from Backend.DataTypes.BatchList import BatchList
from Backend.DataTypes.Status import Status



ApplicantDetailsQueryResult = UnionType("ApplicantDetailsQueryResult")
@ApplicantDetailsQueryResult.type_resolver
def resolve_applicant_details_query_result(obj, *_):
    if isinstance(obj, Applicant):
        return "Applicant"
    if isinstance(obj, AuthenticationException):
        return "Exception"
    if isinstance(obj, IncorrectParameterException):
        return "Exception"
    return None


ApplicantsQueryResult = UnionType("ApplicantsQueryResult")
@ApplicantsQueryResult.type_resolver
def resolve_applicants_query_result(obj, *_):
    if isinstance(obj, ApplicantList):
        return "ApplicantList"
    if isinstance(obj, AuthenticationException):
        return "Exception"
    if isinstance(obj, IncorrectParameterException):
        return "Exception"
    return None


BatchesQueryResult = UnionType("BatchesQueryResult")
@BatchesQueryResult.type_resolver
def resolve_batches_query_result(obj, *_):
    if isinstance(obj, BatchList):
        return "BatchList"
    if isinstance(obj, AuthenticationException):
        return "Exception"
    if isinstance(obj, IncorrectParameterException):
        return "Exception"
    return None




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




SendEmailMutationResult = UnionType("SendEmailMutationResult")
@SendEmailMutationResult.type_resolver
def resolve_sendEmail_mutatation_result(obj, *_):
    if isinstance(obj, Status):
        return "Status"
    if isinstance(obj, AuthenticationException):
        return "Exception"
    if isinstance(obj, IncorrectParameterException):
        return "Exception"
    return None



SaveFormMutationResult = UnionType("SaveFormMutationResult")
@SaveFormMutationResult.type_resolver
def resolve_saveForm_mutatation_result(obj, *_):
    if isinstance(obj, Status):
        return "Status"
    if isinstance(obj, AuthenticationException):
        return "Exception"
    if isinstance(obj, IncorrectParameterException):
        return "Exception"
    return None
