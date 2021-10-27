from flask import render_template
from Backend.config import config


def send_form_confirmation(name, track, batch, applicantid, acceptanceFormData):
    subject = "Confirmation!"
    body = render_template('SendFormConfirmation.html', applicantName=name, applicantTrack=track, acceptanceForm=config.ACCEPTANCE_FORM + str(name) + "/" + str(batch) + "/" + str(applicantid),
                           batch=batch,
                           location=acceptanceFormData['location'] if acceptanceFormData else None,
                           streetNumber=acceptanceFormData['streetNumber'] if acceptanceFormData else None,
                           addressSuffix=acceptanceFormData['addressSuffix'] if acceptanceFormData else None,
                           postcode=acceptanceFormData['postcode'] if acceptanceFormData else None,
                           city=acceptanceFormData['city'] if acceptanceFormData else None,
                           country=acceptanceFormData['country'] if acceptanceFormData else None,
                           accountHolder=acceptanceFormData['accountHolder'] if acceptanceFormData else None,
                           bankName=acceptanceFormData['bankName'] if acceptanceFormData else None,
                           iban=acceptanceFormData['iban'] if acceptanceFormData else None,
                           bic=acceptanceFormData['bic'] if acceptanceFormData else None,
                           foodIntolerances=acceptanceFormData['foodIntolerances'] if acceptanceFormData else None,
                           shirtSize=acceptanceFormData['shirtSize'] if acceptanceFormData else None,
                           shirtStyle=acceptanceFormData['shirtStyle'] if acceptanceFormData else None)
    footer = render_template('Footer.html')
    return {"subject": subject, "body": body + footer}
