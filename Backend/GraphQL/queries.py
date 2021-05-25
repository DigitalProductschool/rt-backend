from Backend.DataTypes.AuthenticationException import AuthenticationException
from ariadne import QueryType
from ariadne import UnionType
from Backend.database import db
from Backend.DataTypes.Applicant import Applicant
from Backend.DataTypes.Batch import Batch
from flask import jsonify
from Backend.Authentication.verify_token import get_user_context
from Backend.DataTypes.ApplicantList import ApplicantList
from Backend.DataTypes.BatchList import BatchList

batch_details = db.collection('batch-details')
batches = db.collection('batches')
query = QueryType()


# TODO This method has to change to query only the information that will be displayed on the applicants List
@query.field("applicants")
def resolve_applicants(_, info, batch_id):
    authentication = get_user_context(info)
    if (authentication):
        applicants = []
        applications = batches.document(
            'batch-' + str(batch_id)).collection('applications')
        applications = [doc.to_dict() for doc in applications.stream()]

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
        return AuthenticationException(404, "User does not have permissions")


@query.field("applicantDetails")
def resolve_applicant_details(_, info, batch_id, applicant_id):
    authentication = get_user_context(info)
    if ( not authentication):
        applications = batches.document(
            'batch-' + str(batch_id)).collection('applications')
        applicant = applications.document(str(applicant_id))
        application = applicant.get().to_dict()
        return Applicant(application['id'],
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
    else:
        return AuthenticationException(404, "User does not have permissions")


@query.field("batches")
def resolve_batches(_, info, batch_id):
    authentication = get_user_context(info)
    if (authentication):
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
        return BatchList(batches)
    else:
        return AuthenticationException(404, "User does not have permissions")




ApplicantDetailsQueryResult = UnionType("ApplicantDetailsQueryResult")
@ApplicantDetailsQueryResult.type_resolver
def resolve_applicant_details_query_result(obj, *_):
    if isinstance(obj, Applicant):
        return "Applicant"
    if isinstance(obj, AuthenticationException):
        return "AuthenticationException"
    return None


ApplicantsQueryResult = UnionType("ApplicantsQueryResult")
@ApplicantsQueryResult.type_resolver
def resolve_applicants_query_result(obj, *_):
    if isinstance(obj, ApplicantList):
        return "ApplicantList"
    if isinstance(obj, AuthenticationException):
        return "AuthenticationException"
    return None


BatchesQueryResult = UnionType("BatchesQueryResult")
@BatchesQueryResult.type_resolver
def resolve_batches_query_result(obj, *_):
    if isinstance(obj, BatchList):
        return "BatchList"
    if isinstance(obj, AuthenticationException):
        return "AuthenticationException"
    return None