from Backend.DataTypes.ApplicantList import ApplicantList
from Backend.GraphQL.shared import query, batches, create_applicant, incorrect_parameter
from graphql import GraphQLError
import time

@query.field("applicantsFromTrack")
def resolve_applicant_from_track(_, info, batch_id_list, track_list):
    applicants = []
    for batch_id in batch_id_list:
        print(batch_id)
        for track in track_list:
            print(track)
            batch_doc = batches.document('batch-' + str(batch_id))
            incorrect_parameter(batch_doc)
            applicationsFromStatus = [doc.to_dict() for doc in batch_doc.collection(
                'applications').where('track', '==', track).stream()]

            start = time.time()
            for application in applicationsFromStatus:
                # ugly hack to speed up the application, should respect graphql query instead
                application['cv'] = None
                application['coverLetter'] = None
                applicants.append(create_applicant(application, False))
            end = time.time()

            print(end-start)

    return ApplicantList(applicants)
