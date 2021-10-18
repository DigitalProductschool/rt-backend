from Backend.DataTypes.ApplicantList import ApplicantList
from Backend.GraphQL.shared import query, batches, create_applicant, incorrect_parameter
from graphql import GraphQLError


@query.field("applicantsFromTrack")
def resolve_applicant_from_status(_, info, batch_id_list, track_list):
    applicants = []
    for batch_id in batch_id_list:
        for track in track_list:
            batch_doc = batches.document('batch-' + str(batch_id))
            incorrect_parameter(batch_doc)

            applicationsFromStatus = [doc.to_dict() for doc in batch_doc.collection(
                'applications').where('track', '==', track).stream()]
            for application in applicationsFromStatus:
                applicants.append(create_applicant(application))
    return ApplicantList(applicants)
