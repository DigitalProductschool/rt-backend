from Backend.DataTypes.Emails.GenerateDocs.Shared import css, generate_options
from flask import render_template
import pdfkit
from email.mime.application import MIMEApplication

def generate_scholarship_agreement(program, name, batch, batchTime, scholarship, streetNumber, postcode, city, country, iban, bic, bankName, accountHolder):
    options = generate_options(program)
    document = render_template(program +'/Scholarship.html',
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
    pdfkit.from_string(document, "Scholarship.pdf", options, css=css)
    scholarship_pdf = MIMEApplication(open("Scholarship.pdf", "rb").read())
    scholarship_pdf.add_header('Content-Disposition',
                         'attachment', filename="Scholarship.pdf")
    return scholarship_pdf
