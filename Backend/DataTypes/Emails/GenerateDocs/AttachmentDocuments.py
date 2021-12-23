from Backend.DataTypes.Emails.GenerateDocs.GenerateOfferLetter import generate_offer_letter
from Backend.DataTypes.Emails.GenerateDocs.Shared  import shared_send_email, create_pdf

def attachment_documents_email(program, name, batch, batchTime, scholarship, config_email, dps_email, dps_password, email, track_handle):
    visaFAQ =  create_pdf('static/' + program + '/VisaFAQ.pdf', "VisaFAQ.pdf")
    scholarshipOptions =  create_pdf('static/' + program + '/ScholarshipOptions.pdf', "ScholarshipOptions.pdf")
    trackDescription = create_pdf('static/' + program + '/TrackDescription/' + track_handle + 'TrackDescription.pdf',
               "TrackDescription.pdf")
    offer = generate_offer_letter(program, name, batch, batchTime, scholarship)
    documents = [offer, visaFAQ, scholarshipOptions, trackDescription]
    shared_send_email(config_email, dps_email, dps_password, email, documents)
