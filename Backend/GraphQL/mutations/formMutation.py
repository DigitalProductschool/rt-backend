from Backend.DataTypes.Emails.Email import Email
from Backend.DataTypes.Status import Status
from Backend.GraphQL.shared import mutation, get_applicant_document
from graphql import GraphQLError


@mutation.field("saveForm")
def save_form(_, info,  applicant_id, batch_id, location, streetNumber, addressSuffix, postcode, city, country, accountHolder, bankName, iban, bic, shirtSize, shirtStyle, foodIntolerances):
    try:
        application, _ = get_applicant_document(batch_id, applicant_id)
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
        Email('sendFormConfirmation', applicant_id, batch_id).send_email()
        Email('sendDocuments', applicant_id, batch_id).send_email_with_attach()
        return Status(0, 'Form was succesfully saved & Documents were sent')
