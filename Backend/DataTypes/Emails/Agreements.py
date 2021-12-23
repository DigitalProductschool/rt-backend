from flask import render_template

def send_agreements(name, batch, batchStart):
    subject = "Important agreements in terms of your participation"
    body = render_template(
        'SendAgreementsEmail.html', applicantName=name, batch=batch, batchStart=batchStart)
    footer = render_template('Footer.html')
    return {"subject": subject, "body": body + footer}
