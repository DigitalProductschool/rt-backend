
from Backend.database import access_secret_version
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import random
from flask import render_template
import os 
import pdfkit
from Backend.config import config

class Emails:
    def __init__(self, config, applicantId, applicantName, applicantEmail, applicantTrack, batchNumber):
        self.name = applicantName
        self.id = applicantId
        self.dps_email = access_secret_version('dps-email')
        self.dps_password = access_secret_version('dps-email-pass')
        self.config = config
        self.email = applicantEmail
        self.track = applicantTrack.name
        self.challengeLink = random.choice(applicantTrack.challengeLink)  if applicantTrack.challengeLink else None
        coreTeam = random.choice(applicantTrack.coreTeam)
        self.coreTeamLink = coreTeam["calendly"]
        self.coreTeamName = coreTeam["name"]
        self.acceptanceLink = "acceptanceLink"
        self.batchNumber = str(batchNumber)
        self.qaLink = applicantTrack.qaLink
    
    def config_email(self):
        all_emails = {
            'sendChallenge': self.send_challenge(),
            'sendQ&A': self.send_qa(),
            'sendInvitation': self.invite_to_interview(),
            'sendRejection': self.reject(),
            'sendAcceptance': self.send_acceptance(),
            'sendDocuments': self.send_documents(),
        }
        email = all_emails[self.config]
        return email

    def send_challenge(self):
        subject = "DPS Challenge Assessment"
        body = render_template('SendChallengeEmail.html', applicantName=self.name, applicantTrack=self.track, challengeLink=self.challengeLink)        
        footer = render_template('Footer.html')
        return {"subject": subject, "body": body + footer}

    def send_qa(self):
        subject = "Invitation to Q&A"
        body = render_template('SendQ&AEmail.html', applicantName=self.name, applicantTrack=self.track, qaLink= self.qaLink)        
        footer = render_template('Footer.html')
        return {"subject": subject, "body": body + footer}

    def invite_to_interview(self):
        subject = "Invitation to Interview"
        body = render_template('SendInvitationEmail.html', applicantName=self.name, applicantTrack=self.track, coreTeamLink= self.coreTeamLink, coreTeamName=self.coreTeamName)        
        footer = render_template('Footer.html')
        return {"subject": subject, "body": body + footer}

    def reject(self):
        subject = "Your application for Digital Product School"
        body = render_template('SendRejectionEmail.html', applicantName=self.name, applicantTrack=self.track)
        footer = render_template('Footer.html')
        return {"subject": subject, "body": body + footer}

    def send_acceptance(self):
        subject = "You are accepted!"
        body = render_template('SendAcceptanceEmail.html', applicantName=self.name, applicantTrack=self.track, acceptanceForm=config.ACCEPTANCE_FORM + str(self.name) + "/" + str(self.batchNumber) + "/" + str(self.id) )
        footer = render_template('Footer.html')
        return {"subject": subject, "body": body + footer}

    def send_documents(self):
        subject = "Confirmation & Important Documents"
        body = render_template('SendDocumentsEmail.html', applicantName=self.name, batchNumber=self.batchNumber)
        footer = render_template('Footer.html')
        return {"subject": subject, "body": body + footer}

    def send_email(self):
        msg = MIMEMultipart()
        msg_template = self.config_email()
        msg['Subject'] = msg_template["subject"]
        msg['From'] = f"DPS Applications{self.dps_email}"
        msg['To'] = self.email
        body = MIMEText(msg_template["body"], 'html')
        msg.attach(body)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.dps_email, self.dps_password)
            smtp.send_message(msg)

    def read_file_path(self, filelocation): 
        root = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(root, filelocation)
        return file_path

    def attach_pdf(self, filelocation, filename, msg):
        pdf_path = self.read_file_path(filelocation)
        pdf = MIMEApplication(open(pdf_path,"rb").read())
        pdf.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(pdf)
        return pdf

    def generate_offer_letter(self):
        options = {
         "enable-local-file-access": None }
        css_file = self.read_file_path('static/styles.css')
        dps_logo = self.read_file_path('static/dps.png')
        utum_logo = self.read_file_path('static/utum.png')
        signature = self.read_file_path('static/thomas-signature.png')
        document = render_template('OfferLetter.html', applicantName=self.name, batchNumber=self.batchNumber, batchTime="Nov", dpsLogo=dps_logo, utumLogo=utum_logo, signature=signature)
        css=[css_file]
        pdf = pdfkit.from_string(document,"Output.pdf", options, css=css)

    def send_email_with_attach(self): 
        msg = MIMEMultipart()
        msg_template = self.config_email()
        msg['Subject'] = msg_template["subject"]
        msg['From'] = f"DPS Applications{self.dps_email}"
        msg['To'] = self.email
        body = MIMEText(msg_template["body"], 'html')
        msg.attach(body)
        visa_faq = self.attach_pdf('static/VisaFAQ.pdf',"VisaFAQ.pdf", msg)
        scholarship_options = self.attach_pdf('static/ScholarshipOptions.pdf',"ScholarshipOptions.pdf", msg)
        track_description = self.attach_pdf('static/SETrackDescription.pdf',"TrackDescription.pdf", msg)
        self.generate_offer_letter()
        pdf = MIMEApplication(open("Output.pdf","rb").read())
        pdf.add_header('Content-Disposition', 'attachment', filename="OfferLetter.pdf")
        msg.attach(pdf)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.dps_email, self.dps_password)
            smtp.send_message(msg)