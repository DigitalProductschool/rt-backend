from Backend.GraphQL.shared import mutation, get_applicant_document
from Backend.DataTypes.Status import Status
from graphql import GraphQLError

# threshold that if exceeded changed an applicant status to PRETTY_COOL
coolnessThreshold = 3.5
requiredVotesNo = 2  # required number of votes for the threshold to be changed


def config_status(ratings):
    if (len(ratings) >= requiredVotesNo):
        filtered_vals = [v for _, v in ratings.items()]
        average = sum(filtered_vals) / len(filtered_vals)

        if average > coolnessThreshold:
            return "PRETTY COOL"
        else:
            return "NEUTRAL"
    else:
        return "NEW"


@mutation.field("rate")
def resolve_rate(_, info, batch_id, applicant_id, score):
    try:
            application, application_details = get_applicant_document(batch_id, applicant_id)
    except Exception as err:
            return GraphQLError(message=err.__str__())
    try:
            ratings = application_details['ratings']
            ratings[str(current_user.uid)] = score
            application.update({'ratings': ratings})
    except:
            ratings = {}
            ratings[str(current_user.uid)] = score
            application.set({'ratings': ratings}, merge=True)

    status = config_status(ratings)
    application.set({'status': status}, merge=True)

    return Status(0, "User voted sucessfuly")