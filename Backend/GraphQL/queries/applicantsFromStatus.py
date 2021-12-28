from Backend.DataTypes.ApplicantList import ApplicantList
from Backend.GraphQL.shared import query, batches, create_applicant, incorrect_parameter
from graphql import GraphQLError


@query.field("applicantsFromStatus")
def resolve_applicant_from_status(_, info, batch_id_list, status_list):
    applicants = []
    for batch_id in batch_id_list:
        for status in status_list:
            batch_doc = batches.document('batch-' + str(batch_id))
            incorrect_parameter(batch_doc)

            applicationsFromStatus = [doc.to_dict() for doc in batch_doc.collection(
                'applications').where('status', '==', status).stream()]
            for application in applicationsFromStatus:
                applicants.append(create_applicant(application, False))
    return ApplicantList(applicants)
