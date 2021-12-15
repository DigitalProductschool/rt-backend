from Backend.GraphQL.shared import mutation, get_applicant_document, get_batch_document, update_status
from Backend.GraphQL.mutations.statusMutation import mutation_status
from Backend.DataTypes.Status import Status
from Backend.DataTypes.Emails.Email import Email
from graphql import GraphQLError


def config_status(email_type):
    all_emails = {
        'sendPromising': 'Promising Sent',
        'sendChallenge': 'Challenge Sent',
        'sendQ&A': 'Q&A Sent',
        'sendInvitation': 'Invitation Sent',
        'sendRejection': 'Rejected',
        'sendWaitingList': 'Waiting List Sent',
        'sendAcceptance': 'Accepted',
        'sendFormConfirmation': 'Form Filled',
        'sendDocuments': 'Documents Sent',
        'sendAgreements': 'Agreements Sent'
    }
    status = all_emails[email_type]
    return status


@mutation.field("sendEmail")
def mutation_email(_, info, email_type, applicant_id, batch_id):
    additional_info = ""
    application, application_details = get_applicant_document(
        batch_id, applicant_id)
    if not application:
        return GraphQLError(message="Applicant with this id does not exist")
    status = config_status(email_type)
    mutation_status(_, info, applicant_id, batch_id, status)
    Email(email_type, application_details).send_email()
    return Status(0, 'Email was succesfuly sent ' + additional_info)
