from Backend.Authentication.verify_token import get_user_context
from Backend.DataTypes.Exceptions.AuthenticationException import AuthenticationException
from Backend.DataTypes.Exceptions.IncorrectParameterException import IncorrectParameterException

from Backend.GraphQL.shared import mutation, get_applicant_document
from Backend.DataTypes.Status import Status
from Backend.emails import Emails
from Backend.tracks import SE, AI, PM, IxD, AC, PMC

def config_status(email_type):
        all_emails = {
            'sendPromising': 'Promising Sent',
            'sendDocuments': 'Documents Sent',
            'sendChallenge': 'Challenge Sent',
            'sendQ&A': 'Q&A Sent',
            'sendInvitation': 'Invitation Sent',
            'sendRejection': 'Rejected',
            'sendAcceptance': 'Accepted',
            'sendFormConfirmation' : 'Form Filled'
        }
        status = all_emails[email_type]
        return status

def config_track(track):
        all_tracks = {
            'se': SE,
            'ai': AI,
            'pm': PM,
            'ixd': IxD,
            'ac': AC,
            'pmc': PMC,
        }
        track = all_tracks[track]
        return track

@mutation.field("updateStatus")   
def mutation_status(_, info, applicant_id, batch_id, status):
    current_user = get_user_context(info)
    if(current_user):
        try:
            application, application_details = get_applicant_document(info, batch_id, applicant_id)
        except Exception as err:
            return IncorrectParameterException(errorMessage=err.__str__())

        if(application):
            application.update({'status': status})
            return Status(0,'Status was updated succesfuly')

    else:
        return AuthenticationException()


@mutation.field("sendEmail")
def mutation_email(_, info, applicant_id, email_type, applicant_name, applicant_email, track, batch_id):
    current_user = get_user_context(info)
    # current_user = User(123663, "Magda", "ntmagda393@gmail.com", "photo")
    if(current_user):
        try:
            application, application_details = get_applicant_document(info, batch_id, applicant_id)
        except Exception as err:
            return IncorrectParameterException(errorMessage=err.__str__())

        if(application):
            status = config_status(email_type)      
            application.update({'status': status})
            track_class = config_track(track)
            if status == 'Documents Sent':
                # to be refarctored to get Applicant class
                Emails(email_type, applicant_id, applicant_name, applicant_email, track_class, batch_id, None).send_email_with_attach()
            else:
                Emails(email_type, applicant_id, applicant_name, applicant_email, track_class, batch_id, None).send_email()
            return Status(0,'Email was succesfuly sent')

    else:
        return AuthenticationException()
