from Backend.DataTypes.Emails.GenerateDocs.Shared import css, generate_options
from flask import render_template
import pdfkit
from email.mime.application import MIMEApplication

def generate_participation_agreement(program, name, streetNumber, postcode, city, country):
    options = generate_options(program)
    document = render_template(program +'/Participation.html',
                               applicantName=name,
                               streetNumber=streetNumber,
                               postcode=postcode,
                               city=city,
                               country=country,
                               )
    pdfkit.from_string(document, "Participation.pdf", options, css=css)
    participation_pdf = MIMEApplication(open("Participation.pdf", "rb").read())
    participation_pdf.add_header('Content-Disposition',
                         'attachment', filename="Participation.pdf")
    return participation_pdf       
