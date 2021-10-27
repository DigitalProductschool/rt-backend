from flask import render_template

def send_documents(name, batch):
    subject = "Important Documents"
    body = render_template(
        'SendDocumentsEmail.html', applicantName=name, batch=batch)
    footer = render_template('Footer.html')
    return {"subject": subject, "body": body + footer}
