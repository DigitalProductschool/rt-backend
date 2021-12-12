from Backend.database import access_secret_version
from Backend.GraphQL.shared import get_applicant_document
from Backend.DataTypes.Emails.Promising import send_promising
from Backend.DataTypes.Emails.Challenge import send_challenge
from Backend.DataTypes.Emails.QA import send_qa
from Backend.DataTypes.Emails.InviteInterview import invite_to_interview
from Backend.DataTypes.Emails.Reject import reject
from Backend.DataTypes.Emails.Accept import send_acceptance
from Backend.DataTypes.Emails.FormConfirmation import send_form_confirmation
from Backend.DataTypes.Emails.Documents import send_documents
from Backend.DataTypes.Emails.WaitingList import send_waiting_list
from Backend.DataTypes.Track import Track, TrackDetails
from Backend.DataTypes.Emails.Scholarship import config_scholarship
import random
from Backend.DataTypes.Emails.SimpleEmail import simple_email
from Backend.DataTypes.Emails.AttachmentEmail import attachment_email

class Email:
    def __init__(self, config, applicant_details):

        self.dps_email = access_secret_version('dps-email')
        self.dps_password = access_secret_version('dps-email-pass')
        self.config = config
        self.name = applicant_details["name"]
        self.id = applicant_details["id"]
        self.email = applicant_details["email"]
        self.batch = applicant_details["batch"]
        self.acceptanceFormData = applicant_details["acceptanceFormData"] if "acceptanceFormData" in applicant_details else None

        track_details = TrackDetails(Track[applicant_details["track"]])
        self.track = track_details.name
        self.track_handle = track_details.handle
        self.qaLink = track_details.qaLink
        self.challengeLink = random.choice(track_details.challengeLink) if track_details.challengeLink else None

        coreTeam = random.choice(track_details.coreTeam)
        self.coreTeamLink = coreTeam.calendly
        self.coreTeamName = coreTeam.name
        self.batchStart = "January 17, 2022"  
        self.batchTime="January 17, 2022 to April 8, 2022"

    # To be refactored again in the future -> to no pass so many 
    def create_template(self):
        all_emails = {
            'sendPromising': send_promising(self.name, self.track),
            'sendChallenge': send_challenge(self.name, self.track, self.challengeLink),
            'sendQ&A': send_qa(self.name, self.track, self.qaLink),
            'sendInvitation': invite_to_interview(self.name, self.track, self.coreTeamLink, self.coreTeamName),
            'sendRejection': reject(self.name, self.track),
            'sendWaitingList': send_waiting_list(self.name, self.track, self.batch, self.batchStart, self.coreTeamName),
            'sendAcceptance': send_acceptance(self.name, self.track, self.batch, self.id),
            'sendFormConfirmation': send_form_confirmation(self.name, self.track, self.batch, self.id, self.acceptanceFormData),
            'sendDocuments': send_documents(self.name, self.batch),
         }
        email = all_emails[self.config]
        return email


    def send_email(self):
        if self.config == 'sendDocuments':
            attachment_email(self.name, self.batch, self.batchTime, config_scholarship(self.acceptanceFormData["location"],  self.acceptanceFormData["country"]),
                             self.create_template(), self.dps_email, self.dps_password, self.email, self.track_handle)
        else:
            simple_email(self.create_template(), self.dps_email, self.dps_password, self.email)
