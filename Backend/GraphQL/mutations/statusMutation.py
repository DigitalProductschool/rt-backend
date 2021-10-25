
from Backend.GraphQL.shared import mutation, get_applicant_document, update_status, get_current_user
from Backend.DataTypes.Status import Status
from graphql import GraphQLError

@mutation.field("updateStatus")
def mutation_status(_, info, applicant_id, batch_id, status):
    get_current_user(info)
    try:
        application, _ = get_applicant_document(batch_id, applicant_id)
    except Exception as err:
        return GraphQLError(message=err.__str__())

    if(application):
       return update_status(application, status)

# We need to disable sending any type of status
# NEW - the applicant just applied
# Promising Sent - the email that the application is promising is sent
# Challenge Sent - the challenge was sent to applicant
# Q&ASent - the q&a link was sent
# Invitation Sent - invitation link to 1-1 sent
# Interview Scheduled - interview was scheduled
# Interview Done - interview was done
# Accepted - applicant accepted
# Form Filled - applicant filled the form
# Document Sents - applicant received the documents
# Rejected - applicant rejected
# Waiting List Sent - the applicant is in waiting list
# Duplicated - used to mark duplicated applications