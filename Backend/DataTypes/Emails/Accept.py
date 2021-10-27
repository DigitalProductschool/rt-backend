from flask import render_template
from Backend.config import config


def send_acceptance(name, track, batch, applicantid):
    subject = "You are accepted!"
    body = render_template('SendAcceptanceEmail.html', applicantName=name, applicantTrack=track,
                           acceptanceForm=config.ACCEPTANCE_FORM + str(name) + "/" + str(batch) + "/" + str(applicantid))
    footer = render_template('Footer.html')
    return {"subject": subject, "body": body + footer}
