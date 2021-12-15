
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
        "enable-local-file-access": None,
        "--header-html": file_path('static/PDFHeader.html') ,
        "--footer-html": file_path('static/PDFFooter.html'),
        "--margin-left": "20mm", 
        "--margin-right": "20mm",
        "--margin-top": "40mm",
        "--margin-bottom": "40mm",}
    css_file = file_path('static/styles.css')
    signature = file_path('static/thomas-signature.png')
    document = render_template('OfferLetter.html',
                               applicantName=name,
                               batch=batch,
                               batchTime=batchTime,
                               signature=signature,
                               scholarship=scholarship.offerDescription)
    css = [css_file]
    pdfkit.from_string(document, "Offer.pdf", options, css=css)

def generate_scholarship_agreement(name, batch, batchTime, scholarship, streetNumber,postcode, city, country, iban, bic, bankName, accountHolder):
    options = {
        "enable-local-file-access": None,
        "--header-html": file_path('static/PDFHeader.html') ,
        "--footer-html": file_path('static/PDFFooter.html'),
        "--margin-left": "20mm", 
        "--margin-right": "20mm",
        "--margin-top": "40mm",
        "--margin-bottom": "40mm",
        }
    css_file = file_path('static/styles.css')
    document = render_template('Scholarship.html',
                               applicantName=name,
                               type=scholarship.name,
                               streetNumber=streetNumber,
                               postcode=postcode,
                               city=city,
                               country=country,
                               batchTime=batchTime,
                               totalAmount= scholarship.totalAmount,
                               monthlyAmount=scholarship.monthlyAmount,
                               bankAmount=scholarship.bankAmount,
                               iban=iban,
                               bic=bic,
                               bankName=bankName,
                               accountHolder=accountHolder,
                               )
    css = [css_file]
    pdfkit.from_string(document, "Scholarship.pdf", options, css=css)


def generate_participation_agreement(name, streetNumber, postcode, city, country):
    options = {
        "enable-local-file-access": None,
        "--header-html": file_path('static/PDFHeader.html'),
        "--footer-html": file_path('static/PDFFooter.html'),
        "--margin-left": "20mm", 
        "--margin-right": "20mm",
        "--margin-top": "40mm",
        "--margin-bottom": "40mm",
        }
    css_file = file_path('static/styles.css')
    document = render_template('Participation.html',
                               applicantName=name,
                               streetNumber=streetNumber,
                               postcode=postcode,
                               city=city,
                               country=country,
                               )
    css = [css_file]
    pdfkit.from_string(document, "Participation.pdf", options, css=css)


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

def attachment_agreements_email(name, batch, batchTime, scholarship, acceptanceFormData, config_email, dps_email, dps_password, email):
    msg = MIMEMultipart()
    msg_template = config_email
    msg['Subject'] = msg_template["subject"]
    msg['From'] = f"DPS Applications{dps_email}"
    msg['To'] = email
    body = MIMEText(msg_template["body"], 'html')
    msg.attach(body)
    # Scholarship
    generate_scholarship_agreement(name, batch, batchTime, scholarship, acceptanceFormData["streetNumber"], acceptanceFormData["postcode"], acceptanceFormData["city"], acceptanceFormData["country"], acceptanceFormData["iban"], acceptanceFormData["bic"], acceptanceFormData["bankName"], acceptanceFormData["accountHolder"] )
    scholarship_pdf = MIMEApplication(open("Scholarship.pdf", "rb").read())
    scholarship_pdf.add_header('Content-Disposition',
                         'attachment', filename="Scholarship.pdf")
    msg.attach(scholarship_pdf)
    # Participation
    generate_participation_agreement(name, acceptanceFormData["streetNumber"], acceptanceFormData["postcode"], acceptanceFormData["city"], acceptanceFormData["country"] )
    participation_pdf = MIMEApplication(open("Participation.pdf", "rb").read())
    participation_pdf.add_header('Content-Disposition',
                         'attachment', filename="Participation.pdf")
    msg.attach(participation_pdf)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(dps_email, dps_password)
        smtp.send_message(msg)