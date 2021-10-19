from flask import render_template
from Backend.config import config


def send_form_confirmation(name, track, batch, applicantid, acceptanceFormData):
    subject = "Confirmation!"
    body = render_template('SendFormConfirmation.html', applicantName=name, applicantTrack=track, acceptanceForm=config.ACCEPTANCE_FORM + str(name) + "/" + str(batch) + "/" + str(applicantid),
                           batch=batch,
                           location=acceptanceFormData['location'],
                           streetNumber=acceptanceFormData['streetNumber'],
                           addressSuffix=acceptanceFormData['addressSuffix'],
                           postcode=acceptanceFormData['postcode'],
                           city=acceptanceFormData['city'],
                           country=acceptanceFormData['country'],
                           accountHolder=acceptanceFormData['accountHolder'],
                           bankName=acceptanceFormData['bankName'],
                           iban=acceptanceFormData['iban'],
                           bic=acceptanceFormData['bic'],
                           foodIntolerances=acceptanceFormData['foodIntolerances'],
                           shirtSize=acceptanceFormData['shirtSize'],
                           shirtStyle=acceptanceFormData['shirtStyle'])
    footer = render_template('Footer.html')
    return {"subject": subject, "body": body + footer}
