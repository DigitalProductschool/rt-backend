
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os
from flask import render_template
import pdfkit


def file_path(filelocation):
    root = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(root, filelocation)
    return file_path


def attach_pdf(filelocation, filename, msg):
    pdf_path = file_path(filelocation)
    pdf = MIMEApplication(open(pdf_path, "rb").read())
    pdf.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(pdf)
    return pdf


def generate_offer_letter(name, batch, batchTime, scholarship):
    options = {
        "enable-local-file-access": None}
    css_file = file_path('static/styles.css')
    dps_logo = file_path('static/dps.png')
    utum_logo = file_path('static/utum.png')
    signature = file_path('static/thomas-signature.png')
    document = render_template('OfferLetter.html',
                               applicantName=name,
                               batch=batch,
                               batchTime=batchTime,
                               dpsLogo=dps_logo,
                               utumLogo=utum_logo,
                               signature=signature,
                               scholarship=scholarship)
    css = [css_file]
    pdfkit.from_string(document, "Offer.pdf", options, css=css)


def attachment_email(name, batch, batchTime, scholarship, config_email, dps_email, dps_password, email, track_handle):
    msg = MIMEMultipart()
    msg_template = config_email
    msg['Subject'] = msg_template["subject"]
    msg['From'] = f"DPS Applications{dps_email}"
    msg['To'] = email
    body = MIMEText(msg_template["body"], 'html')
    msg.attach(body)
    attach_pdf('static/VisaFAQ.pdf', "VisaFAQ.pdf", msg)
    attach_pdf('static/ScholarshipOptions.pdf', "ScholarshipOptions.pdf", msg)
    attach_pdf('static/' + track_handle + 'TrackDescription.pdf',
               "TrackDescription.pdf", msg)
    generate_offer_letter(name, batch, batchTime, scholarship)
    offer_pdf = MIMEApplication(open("Offer.pdf", "rb").read())
    offer_pdf.add_header('Content-Disposition',
                         'attachment', filename="OfferLetter.pdf")
    msg.attach(offer_pdf)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(dps_email, dps_password)
        smtp.send_message(msg)
