from ariadne import MutationType
from ariadne import UnionType

from Backend.database import access_secret_version, db
from Backend.DataTypes.Status import Status
from Backend.DataTypes.User import User

from Backend.Authentication.verify_token import get_user_context
from Backend.DataTypes.Exceptions.AuthenticationException import AuthenticationException
from Backend.DataTypes.Exceptions.IncorrectParameterException import IncorrectParameterException

from trello import TrelloClient, Board, Card, List
import os
from Backend.config import Config, config
import smtplib
from email.message import EmailMessage
from Backend.emails import Emails


batch_details = db.collection('batch-details')
batches = db.collection('batches')
mutation = MutationType()

coolnessThreshold = 3.5 # threshold that if exceeded changed an applicant status to PRETTY_COOL
requiredVotesNo = 2 # required number of votes for the threshold to be changed

def get_applicant_document(info, batch_id, applicant_id): 
    current_user = get_user_context(info)
    if(current_user):
        batch_doc = batches.document('batch-' + str(batch_id))
        if not batch_doc.get().exists:
            return IncorrectParameterException(errorMessage='Invalid batch_id')
            
        applications = batch_doc.collection('applications')  
        application = applications.document(str(applicant_id)) 
        if not application.get().exists:
            return IncorrectParameterException(errorMessage='Invalid applicant_id')

        application_details = application.get().to_dict()
        return application, application_details

@mutation.field("rate")
def resolve_rate(_, info, batch_id, applicant_id, score):
    current_user = get_user_context(info)
    # to be refactored
    # current_user = User(123323549339,"Magda", "ntmagda393@gmail.com", "photo")
    if(current_user):
        batch_doc = batches.document('batch-' + str(batch_id))
        if not batch_doc.get().exists:
            return IncorrectParameterException(errorMessage='Invalid batch_id')
            
        applications = batch_doc.collection('applications')        
        application = applications.document(str(applicant_id))

        if not application.get().exists:
            return IncorrectParameterException(errorMessage='Invalid applicant_id')

        application_details = application.get().to_dict()
        try:
            ratings = application_details['ratings']
            ratings[str(current_user.uid)] = score
            application.update({'ratings': ratings})
        except:
            ratings = {}
            ratings[str(current_user.uid)] = score
            application.set({'ratings': ratings}, merge=True)

        status = setApplicantStatus(ratings)
        application.set({'status': status}, merge=True)

        return Status(0, "User voted sucessfuly")
    else:
        return AuthenticationException()


@mutation.field("moveTrelloCard")
def resolve_move_trello_card(_, info, source_list_name, dest_list_name, card_name):
    current_user = get_user_context(info)
    if(current_user):
        client = TrelloClient(
            api_key= Config.TRELLO_API_KEY,
            api_secret= Config.TRELLO_API_SECRET,
        )

        hiring_tool_board = Board(client=client, board_id=config.TRELLO_BOARD_ID, name=config.TRELLO_NAME)
        hiring_tool_lists = hiring_tool_board.list_lists()
        try:
            destList = [list for list in hiring_tool_lists if list.name == dest_list_name][0]
            srcList = [list for list in hiring_tool_lists if list.name == source_list_name][0]

            card_to_be_moved = [card for card in srcList.list_cards() if card.name == card_name][0]
            card_to_be_moved.change_list(destList.id)
        except IndexError:
            return IncorrectParameterException()
        return Status(0,'Card was succesfully moved')
    else:
        return AuthenticationException()



def setApplicantStatus(ratings):
    if ( len(ratings) >= requiredVotesNo ):
        filtered_vals = [v for _, v in ratings.items()]
        average = sum(filtered_vals) / len(filtered_vals)

        if average > coolnessThreshold:
            return "PRETTY COOL"
        else:
            return "NEUTRAL"
    else:
        return  "NEW"



RateMutationResult = UnionType("RateMutationResult")
@RateMutationResult.type_resolver
def resolve_rate_mutatation_result(obj, *_):
    if isinstance(obj, Status):
        return "Status"
    if isinstance(obj, AuthenticationException):
        return "Exception"
    if isinstance(obj, IncorrectParameterException):
        return "Exception"
    return None


def config_status(email_type):
        all_emails = {
            'sendChallenge': 'ChallengeSent',
            'sendQ&A': 'Q&ASent',
            'sendInvitation': 'InvitationSent',
            'sendRejection': 'Rejected',
            'sendAcceptance': 'Accepted',
        }
        status = all_emails[email_type]
        return status

@mutation.field("sendEmail")
def mutation_email(_, info, applicant_id, email_type, applicant_name, applicant_email, track, batch_id):
   # to include the resolver
    application, application_details = get_applicant_document(info, batch_id, applicant_id)
    if(application):
      status = config_status(email_type)      
      application.update({'status': status})
      Emails(email_type, applicant_id, applicant_name, applicant_email, track, batch_id).send_email() 


@mutation.field("sendEmailDocuments")
def mutation_email(_, info,  applicant_id, applicant_name, applicant_email, track, batch_id):
    # to include the resolver
    application, application_details = get_applicant_document(info, batch_id, applicant_id)
    if(application):
      status = "DocumentSent"     
      application.update({'status': status})
      Emails("sendDocuments", applicant_id, applicant_name, applicant_email, track, batch_id).send_email_with_attach()
