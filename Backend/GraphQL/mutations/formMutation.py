from Backend.DataTypes.Emails.Email import Email
from Backend.DataTypes.Status import Status
from Backend.GraphQL.shared import mutation, get_applicant_document, get_batch_document
from graphql import GraphQLError
from Backend.GraphQL.mutations.emailMutation import mutation_email

def convert_applicant_to_participant(applicant_id, batch_id, application_details):
    batch_doc = get_batch_document(batch_id)
    participants = batch_doc.collection('participants')
    participants_doc = participants.document(str(applicant_id))
    participants_doc.set(application_details)

@mutation.field("saveForm")
def save_form(_, info,  applicant_id, batch_id, location, streetNumber, addressSuffix, postcode, city, country, accountHolder, bankName, iban, bic, shirtSize, shirtStyle, foodIntolerances):
    try:
        application, application_details = get_applicant_document(batch_id, applicant_id)
    except Exception as err:
        return GraphQLError(message=err.__str__())

    if(application):
        acceptanceFormData = {
            'location': location,
            'streetNumber': streetNumber,
            'addressSuffix': addressSuffix,
            'postcode':  postcode,
            'city': city,
            'country': country,
            'accountHolder': accountHolder,
            'bankName': bankName,
            'iban': iban,
            'bic': bic,
            'shirtSize': shirtSize,
            'shirtStyle': shirtStyle,
            'foodIntolerances': foodIntolerances
        }
        application.set({"acceptanceFormData": acceptanceFormData}, merge=True)
        info.context["user"] = True
        mutation_email(_, info, 'sendFormConfirmation', applicant_id, batch_id)
        mutation_email(_, info, 'sendDocuments', applicant_id, batch_id)
        convert_applicant_to_participant(applicant_id, batch_id, application_details)
        return Status(0, 'Form was succesfully saved & Documents were sent')
