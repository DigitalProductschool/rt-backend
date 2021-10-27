
from Backend.DataTypes.Applicant import Applicant
from Backend.DataTypes.ApplicantList import ApplicantList
from Backend.GraphQL.shared import query, batches, incorrect_parameter, create_applicant
from graphql import GraphQLError



@query.field("applicants")
def resolve_applicants(_, info, batch_id_list):
    applicants = []

    for batch_id in batch_id_list:
        batch_doc = batches.document('batch-' + str(batch_id))
        incorrect_parameter(batch_doc)

        applications = batch_doc.collection('applications')
        applications = [doc.to_dict() for doc in applications.stream()]
        for application in applications:
            applicants.append(create_applicant(application))
    return ApplicantList(applicants)
