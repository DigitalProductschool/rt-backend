
import imp
from Backend.DataTypes.Applicant import Applicant
from Backend.DataTypes.ApplicantList import ApplicantList
from Backend.GraphQL.shared import query, batches, incorrect_parameter, create_applicant
from graphql import GraphQLError
from Backend.repositories.applicants.FirestoreApplicantRepository import FirestoreApplicantRepository
from Backend.database import db



@query.field("applicants")
def resolve_applicants(_, info, batch_id_list):
    applicantRepository = FirestoreApplicantRepository(db)
    res = applicantRepository.get_all_from_batch_list(batch_id_list)
    if not res:
        raise GraphQLError(message="Incorrect parameter")
    return res