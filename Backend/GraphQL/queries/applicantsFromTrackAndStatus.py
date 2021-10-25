from Backend.DataTypes.ApplicantList import ApplicantList
from Backend.GraphQL.shared import query, batches, create_applicant, incorrect_parameter
from Backend.GraphQL.queries.applicantsFromTrack import resolve_applicant_from_track
from graphql import GraphQLError


@query.field("applicantsFromTrackAndStatus")
def resolve_applicant_from_track_and_status(_, info, batch_id_list, track_list, status_list):
    result = resolve_applicant_from_track(_, info, batch_id_list, track_list)
    if isinstance(result, ApplicantList):
        applicants = result.list
        applicants_by_status = [applicant for applicant in applicants if applicant.status in status_list]
        return ApplicantList(applicants_by_status)
    else: 
        return resolve_applicant_from_track(_, info, batch_id_list, track_list)