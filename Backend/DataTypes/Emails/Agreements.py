from flask import render_template

def send_agreements(name, batch):
    subject = "Important agreements in terms of your participation"
    body = render_template(
        'SendAgreementsEmail.html', applicantName=name, batch=batch)
    footer = render_template('Footer.html')
    return {"subject": subject, "body": body + footer}
