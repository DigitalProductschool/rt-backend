from Backend.DataTypes.Exceptions.IncorrectParameterException import IncorrectParameterException
from Backend.DataTypes.Exceptions.AuthenticationException import AuthenticationException
from ariadne import QueryType
from ariadne import UnionType
from Backend.database import db
from Backend.DataTypes.Applicant import Applicant
from Backend.DataTypes.Batch import Batch
from flask import jsonify
from Backend.Authentication.verify_token import get_user_context
from Backend.DataTypes.ApplicantList import ApplicantList
from Backend.DataTypes.BatchList import BatchList

batches_details = db.collection('batch-details')
batches = db.collection('batches')
query = QueryType()

@query.field("user")
def resolve_current_user(_, info):
     authentication = get_user_context(info)
     return authentication
   

# TODO This method has to change to query only the information that will be displayed on the applicants List
@query.field("applicants")
def resolve_applicants(_, info, batch_id):
    current_user = get_user_context(info)
    if (current_user):
        applicants = []
        batch_doc = batches.document('batch-' + str(batch_id))
        if not batch_doc.get().exists:
            return IncorrectParameterException(errorMessage='Incorrect batch_id parameter')
        applications = batch_doc.collection('applications')
        applications = [doc.to_dict()  for doc in applications.stream()]

        for application in applications:
            applicant = Applicant(application['id'],
                                application['name'],
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
        return ApplicantList(applicants)
    else:
        return AuthenticationException()


@query.field("applicantDetails")
def resolve_applicant_details(_, info, batch_id, applicant_id):
    current_user = get_user_context(info)
    if (current_user):
        batch_doc = batches.document('batch-' + str(batch_id))
        if not batch_doc.get().exists:
            return IncorrectParameterException(errorMessage='Incorrect batch_id parameter')

        applications = batch_doc.collection('applications')
        application = applications.document(str(applicant_id))
        if not application.get().exists:
            return IncorrectParameterException(errorMessage='Incorrect applicant_id')

        applicant = application.get().to_dict()
        return Applicant(applicant['id'],
                                applicant['name'],
                                applicant['batch'],
                                applicant['track'],
                                applicant['email'],
                                applicant['consent'],
                                applicant['coverLetter'],
                                applicant['cv'],
                                applicant['scholarship'],
                                applicant['source'],
                                applicant['gender']
                                )
    else:
        return AuthenticationException()


@query.field("batches")
def resolve_batches(_, info, batch_id):
    current_user = get_user_context(info)
    if (current_user):
      batches = []
      if batch_id:
        batch_details_doc = batches_details.document(str(batch_id))
        if not batch_details_doc.get().exists:
            return IncorrectParameterException(errorMessage='Incorrect batch_id')

        batch_details = batch_details_doc.get().to_dict()
        batch = Batch(batch_details['batch'],
                    batch_details['startDate'],
                    batch_details['endDate'],
                    batch_details['appStartDate'],
                    batch_details['appEndDate'],
                    batch_details['appEndDate-ai'],
                    batch_details['appEndDate-ixd'],
                    batch_details['appEndDate-pm'],
                    batch_details['appEndDate-se']
                    )
        batches.append(batch)
        return BatchList(batches)
      else:
            batches_collection = [doc.to_dict() for doc in batches_details.stream()]
            for batch_details in batches_collection:
                batch = Batch(batch_details['batch'],
                      batch_details['startDate'],
                      batch_details['endDate'],
                      batch_details['appStartDate'],
                      batch_details['appEndDate'],
                      batch_details['appEndDate-ai'],
                      batch_details['appEndDate-ixd'],
                      batch_details['appEndDate-pm'],
                      batch_details['appEndDate-se']
                      )
                batches.append(batch)
            return BatchList(batches)
    else:
        return AuthenticationException()



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

