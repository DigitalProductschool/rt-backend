from Backend.DataTypes.Emails.GenerateDocs.GenerateParticipationAgreement import generate_participation_agreement
from Backend.DataTypes.Emails.GenerateDocs.GenerateScholarshipAgreement import generate_scholarship_agreement
from Backend.DataTypes.Emails.GenerateDocs.Shared  import shared_send_email

def attachment_agreements_email(program, name, batch, batchTime, scholarship, acceptanceFormData, config_email, dps_email, dps_password, email):
    participation = generate_participation_agreement(program, name, acceptanceFormData["streetNumber"], acceptanceFormData["postcode"], acceptanceFormData["city"], acceptanceFormData["country"])
    scholarship =  generate_scholarship_agreement(program, name, batch, batchTime, scholarship, acceptanceFormData["streetNumber"], acceptanceFormData["postcode"], acceptanceFormData["city"], acceptanceFormData["country"], acceptanceFormData["iban"], acceptanceFormData["bic"], acceptanceFormData["bankName"], acceptanceFormData["accountHolder"])
    documents = [scholarship, participation]
    shared_send_email(config_email, dps_email, dps_password, email, documents)
