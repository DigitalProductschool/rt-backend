from Backend.Authentication.verify_token import get_user_context
from Backend.DataTypes.Exceptions.IncorrectParameterException import IncorrectParameterException
from Backend.DataTypes.Exceptions.AuthenticationException import AuthenticationException

from Backend.DataTypes.Applicant import Applicant
from Backend.GraphQL.shared import query, batches

@query.field("applicantDetails")
def resolve_applicant_details(_, info, batch_id, applicant_id):
    current_user = get_user_context(info)
    if (current_user):
        batch_doc = batches.document('batch-' + str(batch_id))
        if not batch_doc.get().exists:
            return IncorrectParameterException(errorMessage='Incorrect batch_id parameter')

        applications = batch_doc.collection('applications')
        application = applications.document(str(applicant_id))
        if not application.get().exists:
            return IncorrectParameterException(errorMessage='Incorrect applicant_id')

        applicant = application.get().to_dict()
        try:
            return Applicant(applicant['id'],
                                    applicant['name'],
                                    applicant['batch'],
                                    applicant['track'],
                                    applicant['email'],
                                    applicant['consent'],
                                    applicant['coverLetter'],
                                    applicant['cv'],
                                    applicant['scholarship'],
                                    applicant['source'],
                                    applicant['gender'],
                                    None,
                                    applicant['status']
                                    )
        except KeyError as err:
                return IncorrectParameterException(1, "The field" + str(err) + "does not exists in the database document" )
    else:
        return AuthenticationException()


