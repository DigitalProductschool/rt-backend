
from Backend.Authentication.verify_token import get_user_context
from Backend.DataTypes.Exceptions.IncorrectParameterException import IncorrectParameterException
from Backend.DataTypes.Exceptions.AuthenticationException import AuthenticationException

from Backend.DataTypes.Applicant import Applicant
from Backend.DataTypes.ApplicantList import ApplicantList
from Backend.GraphQL.shared import query, batches

@query.field("applicants")
def resolve_applicants(_, info, batch_id_list):
    current_user = get_user_context(info)
    applicants = []
    if (current_user):
        for batch_id in batch_id_list:
            batch_doc = batches.document('batch-' + str(batch_id))
            if not batch_doc.get().exists:
                return IncorrectParameterException(errorMessage='Incorrect batch_id parameter')
            applications = batch_doc.collection('applications')
            applications = [doc.to_dict()  for doc in applications.stream()]

            for application in applications:
                try:
                    applicants.append(Applicant(application['id'],
                                        application['name'],
                                        application['batch'],
                                        application['track'],
                                        application['email'],
                                        application['consent'],
                                        application['coverLetter'],
                                        application['cv'],
                                        application['scholarship'],
                                        application['source'],
                                        application['gender'], 
                                        application['acceptanceFormData'] if 'acceptanceFormData' in application else None,
                                        application['status']
                                        ))
                except KeyError as err:
                    return IncorrectParameterException(1, "The field" + str(err) + "does not exists in the database document" )
        return ApplicantList(applicants)
    else:
        return AuthenticationException()