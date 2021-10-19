
from Backend.GraphQL.shared import mutation, get_applicant_document, update_status
from Backend.DataTypes.Status import Status
from graphql import GraphQLError

@mutation.field("updateStatus")
def mutation_status(_, info, applicant_id, batch_id, status):
    try:
        application, _ = get_applicant_document(batch_id, applicant_id)
    except Exception as err:
        return GraphQLError(message=err.__str__())

    if(application):
       update_status(application, status)
