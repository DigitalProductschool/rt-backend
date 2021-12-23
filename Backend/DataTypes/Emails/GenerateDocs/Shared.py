
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


css_file = file_path('static/styles.css')
css = [css_file]

signature = file_path('static/thomas-signature.png')


def create_pdf(filelocation, filename):
    pdf_path = file_path(filelocation)
    pdf = MIMEApplication(open(pdf_path, "rb").read())
    pdf.add_header('Content-Disposition', 'attachment', filename=filename)
    return pdf

def generate_options(program):
    options = {
        "enable-local-file-access": None,
        "--header-html": file_path('static/'+ program + '/Pdf/Header.html'),
        "--footer-html": file_path('static/'+ program + '/Pdf/Footer.html'),
        "--margin-left": "20mm", 
        "--margin-right": "20mm",
        "--margin-top": "40mm",
        "--margin-bottom": "40mm",
        }
    return options
    
def shared_send_email(config_email, dps_email, dps_password, email, documents):
    msg = MIMEMultipart()
    msg_template = config_email
    msg['Subject'] = msg_template["subject"]
    msg['From'] = f"DPS Applications{dps_email}"
    msg['To'] = email
    body = MIMEText(msg_template["body"], 'html')
    msg.attach(body)
    for document in documents: 
         msg.attach(document)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(dps_email, dps_password)
        smtp.send_message(msg)

