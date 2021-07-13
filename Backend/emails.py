
from Backend.database import access_secret_version
import smtplib
from email.message import EmailMessage
import random
from Backend.tracks import se

class Emails:
    footer = "<br><br></p> --<br>\nDigital Product School<br>\nby UnternehmerTUM GmbH<br>\nLichtenbergstr. 6<br>\n85748 Garching bei München<br>\n+49 89-18 94 69-0<br>\n<a href=\"https://www.unternehmertum.de/\">www.unternehmertum.de</a><br>\n<a href=\"https://digitalproductschool.io/\">www.digitalproductschool.io</a><br>\n<a href = \"mailto:hello@dpschool.io\">hello@dpschool.io</a><br><br>\n<a href=\"https://www.facebook.com/digitalproductschool/\"> Facebook </a>|<a href=\"https://twitter.com/dpschool_io\"> Twitter  </a>|<a href=\"https://www.linkedin.com/company/digital-product-school/\"> LinkedIn </a>|<a href=\"https://www.instagram.com/digitalproductschool/\"> Instagram </a>|<a href=\"https://leaks.digitalproductschool.io/\"> Medium </a><br><br>\nManaging Directors:<br>\nProf. Dr. Helmut Schönenberger (CEO), Claudia Frey,<br>\nStefan Drüssler, Thomas Zeller, Dr. Andreas Liebl<br>\nChairwoman of the supervisory board: Susanne Klatten<br>\nRegister Court, Munich: HRB 141703<br>\nVAT: DE 252 789 694"

    def __init__(self, config, applicantName, applicantEmail, applicantTrack, acceptanceLink):
        self.intro = "<p>Hello " + applicantName + ", < br > <br >\n\n"
        self.dps_email = access_secret_version('dps-email')
        self.dps_password = access_secret_version('dps-email-pass')
        self.config = config
        self.applicantEmail = applicantEmail
        self.applicantTrack = applicantTrack
        self.challengeLink = random.choice(SE.challengeLink)
        coreTeam = random.choice(SE.coreTeam)
        self.coreTeamCalendly = coreTeam["calendly"]
        self.coreTeamName = coreTeam["name"]
        self.acceptanceLink = acceptanceLink
        self.batchNumber = 14
        
    def config_email(self):
        all_emails = {
            'sendChallenge': self.send_challenge()
        }
        email = all_emails[self.config]
        return email

    def send_challenge(self):
        subject = "DPS Challenge Assessment"
        body = self.intro + "Thank you for your interest in Digital Product School! <br> <br>\n\nWe are very happy to inform you that we decided to proceed further with your application for the " + self.applicantTrack + " track!<br><br>\n\nThe next step is to complete our technical challenge. You can find more details about the challenge in the following link: <br>\n " + \
            self.challengeLink + "<br><br>\n\nGood Luck! <br><br>\n\n\nYour DPS Team"
        return {"subject": subject, "body": body}

    def invite_to_interview(self):
        subject = "Invitation to Interview"
        body = self.intro + "I’m very happy to inform you that you made it to the last interview step for the " + self.applicantTrack + " track!<br><br>\n\nI would like to invite you for a 30 minute talk and have the opportunity to get to know you better. Please use the following calendly link to schedule a meeting at a convenient time:<br>\n" + \
            self.coreTeamCalendly + "<br><br>\n\nLooking forward to hearing from you! <br><br>\n\n\nCheers,<br>\n" + \
            self.coreTeamName
        return {"subject": subject, "body": body}

    def reject(self):
        subject = "Your application for Digital Product School",
        body = self.intro + "Thank you for your application to the Digital Product School in Munich.\nUnfortunately we cannot move forward with your application for the " + self.applicantTrack + " Track.<br><br>\n\nWhat does that mean?<br>\nWe have a limited number of places and we had a lot of strong applications for this batch, so we have to decline many promising talents. We appreciate the time you’ve invested and we’d like to thank you for giving us the opportunity to learn about your skills and accomplishments. We encourage you to continue building your skills and if you’re still interested in the DPS program, we invite you to apply for our future batches.<br><br>\n\nWe want to draw your attention to <b>another wonderful opportunity</b>:<br><br>\n\nAre you looking for an exciting and startup project?<br>\nDo you have time capacities in the next weeks?<br>\nAre you interested in boosting a startup project as a temporary team member - with the possibility to continue working together after the project period?<br>\nWith UnternehmerTUM’s pre-Incubation Program XPLORE, you have a great possibility to team up with a tech-driven early stage startup for the duration of 8-weeks. During the program, you develop together a valid business model, test market chances and prepare first financing. While doing so, the project teams will be supported through experts and professional coaching sessions.<br><br>\n\nLink to XPLORE: https://www.unternehmertum.de/xplore.html?lang=en <br><br>\n\nThank you and good luck with your future professional endeavors,<br>\nYour DPS team"
        return {"subject": subject, "body": body}

    def send_acceptance(self):
        subject = "You are accepted! :relaxed:",
        body = self.intro + "Thanks for the nice conversation we had! <br><br>\n\nI’m happy to inform you that we have decided to offer you a spot at Digital Product School as a " + self.applicantTrack + "! <br>\nI would be excited if you join us for 3 months of fun and learning.<br><br>\n\nPlease let me know <b>within one week</b>, whether you take part at DPS by <b>clicking this link</b>: <br><br> \n<a href=\" " + \
            self.acceptanceLink + "\"> I accept to be part of DPS</a> <br><br>\n\n</b> Afterwards I will guide you through the next steps.<br><br>\n\nIf you have any questions, please write to support@digitalproductschool.atlassian.net and we’ll get back to you as soon as possible! <br><br>\n\nCheers, <br>\n" + \
            self.coreTeamName
        return {"subject": subject, "body": body}

    def send_documents(self):
        subject = "Confirmation & Important Documents",
        body = self.intro + "Great to see you at Digital Product School Batch# " + self.batchNumber + "!<br><br>\n\nEnclosed you can find some important information:<br>\n<ul>\n<li>Offer Letter: The official confirmation that you will participate in Digital Product School. If you need to apply for a visa, this is the confirmation that you take part in our training program.</li>\n<li>Track Description: This document describes the content of your specific track at DPS. It is mainly for the visa office at the German embassy to provide them further information about our program.</li>\n<li>Visa FAQs: Further information for you with our experiences in the visa process. This should help you to have a smooth process to your visa and may answer a lot of questions you have.</li>\n<li>Scholarship Options: DPS and the scholarships are supported by the Bavarian government. Due to regulations on how to use these grants there are different types regarding the amount. You can find some information and explanation about the different types in this document.</li>\n</ul><br>\n\nIf you have any further questions regarding the documents, please write to support@digitalproductschool.atlassian.net and we’ll get back to you as soon as possible! <br><br>\n\nWe will reach out to you with further information before your batch starts.<br>\n\nCheers,<br>\n" + \
            self.coreTeamName
        return {"subject": subject, "body": body}

    def send_email(self):
        msg = EmailMessage()
        msg_template = self.config_email()
        print(msg_template)
        msg['Subject'] = msg_template["subject"]
        msg['From'] = f"DPS Applications{self.dps_email}"
        msg['To'] = self.applicantEmail
        msg.set_content(msg_template["body"], subtype='html')
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.dps_email, self.dps_password)
            smtp.send_message(msg)
