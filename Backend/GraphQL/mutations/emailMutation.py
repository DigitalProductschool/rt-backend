from Backend.GraphQL.shared import mutation, get_applicant_document, get_batch_document, update_status
from Backend.DataTypes.Status import Status
from Backend.DataTypes.Emails.Email import Email
from graphql import GraphQLError


def config_status(email_type):
    all_emails = {
        'sendPromising': 'Promising Sent',
        'sendDocuments': 'Documents Sent',
        'sendChallenge': 'Challenge Sent',
        'sendQ&A': 'Q&A Sent',
        'sendInvitation': 'Invitation Sent',
        'sendRejection': 'Rejected',
        'sendAcceptance': 'Accepted',
        'sendFormConfirmation': 'Form Filled'
    }
    status = all_emails[email_type]
    return status


def convert_applicant_to_participant(batch_id, applicant_id, application_details):
    batch_doc = get_batch_document(batch_id)
    participants = batch_doc.collection('participants')
    participants_doc = participants.document(str(applicant_id))
    participants_doc.set(application_details)


@mutation.field("sendEmail")
def mutation_email(_, info, email_type, applicant_id, batch_id):
    additional_info = ""
    application, application_details = get_applicant_document(
        batch_id, applicant_id)
    if not application:
        return GraphQLError(message="Applicant with this id does not exist")
    status = config_status(email_type)
    update_status(application, status)
    if status == 'Form Filled':
            convert_applicant_to_participant(
                batch_id, applicant_id, application_details)
            additional_info += ", applicant was marked as a participant"
    elif status == 'Documents Sent':
            Email(email_type, application_details)
    else:
            print('here')
            Email(email_type, application_details)
    return Status(0, 'Email was succesfuly sent ' + additional_info)
