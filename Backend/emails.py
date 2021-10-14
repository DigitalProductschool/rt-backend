
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
    def __init__(self, config, applicant, batch_id, acceptance_form_data):
        self.name = applicant.name
        self.id = applicant.id
        self.email = applicant.email
        self.qaLink = applicant.track.qaLink
        self.track = applicant.track.name
        self.track_handle =  applicant.track.handle
        self.dps_email = access_secret_version('dps-email')
        self.dps_password = access_secret_version('dps-email-pass')
        self.config = config
        self.challengeLink = random.choice(applicant.track.challengeLink)  if applicant.track.challengeLink else None

        coreTeam = random.choice(applicant.track.coreTeam)
        coreTeamEmails = []
        for member in applicant.track.coreTeam: 
             coreTeamEmails.append(member["email"])
             
        self.coreTeamLink = coreTeam["calendly"]
        self.coreTeamName = coreTeam["name"]
        self.coreTeamEmail = coreTeamEmails
        self.acceptanceLink = "acceptanceLink"
        self.batchNumber = str(batch_id)
        self.acceptanceFormData = acceptance_form_data if acceptance_form_data else None


    def config_email(self):
        all_emails = {
            'sendPromising': self.send_promising(),
            'sendChallenge': self.send_challenge(),
            'sendQ&A': self.send_qa(),
            'sendInvitation': self.invite_to_interview(),
            'sendRejection': self.reject(),
            'sendAcceptance': self.send_acceptance(),
            'sendDocuments': self.send_documents(),
            'sendFormConfirmation' : self.send_form_confirmation(),
        }
        email = all_emails[self.config]
        return email

    def config_scholarship(self): 
            oecd_country = ["Australia", "Austria", "Belgium", "Canada", "Chile", "Colombia", "Costa Rica", "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Israel", "Italy", "Japan", "Korea", "Latvia", "Lithuania", "Luxembourg", "Mexico", "Netherlands", "New Zealand", "Norway", "Poland", "Portugal", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom", "United Stated" ]
            if self.acceptanceFormData["location"] == "Munich" if self.acceptanceFormData else None: 
                scholarship_option = "You will also receive a monthly scholarship of 750€."
            elif self.acceptanceFormData["country"] in oecd_country if self.acceptanceFormData else None: 
                scholarship_option = "You will also receive a monthly scholarship of 500€."
            else: 
                scholarship_option = "You will also receive a monthly scholarship of 300.00€  (incl. 50.00€ internet grant)."
            return scholarship_option

    def send_promising(self):
        subject = "Your application for DPS has been reviewed"
        body = render_template('SendPromisingEmail.html', applicantName=self.name, applicantTrack=self.track)        
        footer = render_template('Footer.html')
        return {"subject": subject, "body": body + footer}

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

    def send_form_confirmation(self):
        subject = "Confirmation!"
        body = render_template('SendFormConfirmation.html', applicantName=self.name, applicantTrack=self.track, acceptanceForm=config.ACCEPTANCE_FORM + str(self.name) + "/" + str(self.batchNumber) + "/" + str(self.id), batchNumber = self.batchNumber, location=self.acceptanceFormData['location'] if self.acceptanceFormData else None, streetNumber = self.acceptanceFormData['streetNumber'] if self.acceptanceFormData else None, addressSuffix = self.acceptanceFormData['addressSuffix'] if self.acceptanceFormData else None, postcode= self.acceptanceFormData['postcode'] if self.acceptanceFormData else None, city=self.acceptanceFormData['city'] if self.acceptanceFormData else None, country=self.acceptanceFormData['country'] if self.acceptanceFormData else None, accountHolder=self.acceptanceFormData['accountHolder'] if self.acceptanceFormData else None, bankName=self.acceptanceFormData['bankName'] if self.acceptanceFormData else None, iban=self.acceptanceFormData['iban'] if self.acceptanceFormData else None, bic=self.acceptanceFormData['bic'] if self.acceptanceFormData else None, foodIntolerances=self.acceptanceFormData['foodIntolerances'] if self.acceptanceFormData else None, shirt=self.acceptanceFormData['shirtSize'] if self.acceptanceFormData else None+ " & " + self.acceptanceFormData['shirtStyle'] if self.acceptanceFormData else None )
        footer = render_template('Footer.html')
        return {"subject": subject, "body": body + footer}

    def send_documents(self):
        subject = "Important Documents"
        body = render_template('SendDocumentsEmail.html', applicantName=self.name, batchNumber=self.batchNumber)
        footer = render_template('Footer.html')
        return {"subject": subject, "body": body + footer}

    def send_email(self):
        msg = MIMEMultipart()
        msg_template = self.config_email()
        msg['Subject'] = msg_template["subject"]
        msg['From'] = f"DPS Applications{self.dps_email}"
        msg['To'] = self.email
        msg['Bcc'] = ", ".join(self.coreTeamEmail)
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
        document = render_template('OfferLetter.html', applicantName=self.name, batchNumber=self.batchNumber, batchTime="Nov", dpsLogo=dps_logo, utumLogo=utum_logo, signature=signature, scholarship = self.config_scholarship())
        css=[css_file]
        pdf = pdfkit.from_string(document,"Offer.pdf", options, css=css)

    def generate_scholarship(self):
        options = {
         "enable-local-file-access": None }
        css_file = self.read_file_path('static/styles.css')
        dps_logo = self.read_file_path('static/dps.png')
        utum_logo = self.read_file_path('static/utum.png')
        signature = self.read_file_path('static/thomas-signature.png')
        document = render_template('Scholarship.html', applicantName=self.name, dpsLogo=dps_logo, utumLogo=utum_logo, streetNumber = self.acceptanceFormData['streetNumber'] if self.acceptanceFormData else None, postcode= self.acceptanceFormData['postcode'] if self.acceptanceFormData else None, city=self.acceptanceFormData['city'] if self.acceptanceFormData else None, country=self.acceptanceFormData['country'] if self.acceptanceFormData else None, accountHolder=self.acceptanceFormData['accountHolder'] if self.acceptanceFormData else None, bankName=self.acceptanceFormData['bankName'] if self.acceptanceFormData else None, iban=self.acceptanceFormData['iban'] if self.acceptanceFormData else None, bic=self.acceptanceFormData['bic'] if self.acceptanceFormData else None)
        css=[css_file]
        pdf = pdfkit.from_string(document,"Scholarship.pdf", options, css=css)


    def send_email_with_attach(self): 
        msg = MIMEMultipart()
        msg_template = self.config_email()
        msg['Subject'] = msg_template["subject"]
        msg['From'] = f"DPS Applications{self.dps_email}"
        msg['To'] = self.email
        msg['Bcc'] = ", ".join(self.coreTeamEmail)
        body = MIMEText(msg_template["body"], 'html')
        msg.attach(body)
        visa_faq = self.attach_pdf('static/VisaFAQ.pdf',"VisaFAQ.pdf", msg)
        scholarship_options = self.attach_pdf('static/ScholarshipOptions.pdf',"ScholarshipOptions.pdf", msg)
        track_description = self.attach_pdf('static/' + self.track_handle +'TrackDescription.pdf',"TrackDescription.pdf", msg)
        self.generate_offer_letter()
        self.generate_scholarship()
        offer_pdf = MIMEApplication(open("Offer.pdf","rb").read())
        offer_pdf.add_header('Content-Disposition', 'attachment', filename="OfferLetter.pdf")
        msg.attach(offer_pdf)
       # scholarship_pdf = MIMEApplication(open("Scholarship.pdf","rb").read())
       #  scholarship_pdf.add_header('Content-Disposition', 'attachment', filename="Scholarship.pdf")
       #  msg.attach(scholarship_pdf)
       # include also participation
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.dps_email, self.dps_password)
            smtp.send_message(msg)