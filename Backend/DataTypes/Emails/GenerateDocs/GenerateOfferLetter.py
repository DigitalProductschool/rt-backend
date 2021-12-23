from Backend.DataTypes.Emails.GenerateDocs.Shared import css, signature, generate_options
from flask import render_template
import pdfkit
from email.mime.application import MIMEApplication

def generate_offer_letter(program, name, batch, batchTime, scholarship):
    options = generate_options(program)
    document = render_template(program +'/OfferLetter.html',
                               applicantName=name,
                               batch=batch,
                               batchTime=batchTime,
                               signature=signature,
                               scholarship=scholarship.offerDescription)
    pdfkit.from_string(document, "Offer.pdf", options, css=css)
    offer_pdf = MIMEApplication(open("Offer.pdf", "rb").read())
    offer_pdf.add_header('Content-Disposition',
                         'attachment', filename="OfferLetter.pdf")
    return offer_pdf