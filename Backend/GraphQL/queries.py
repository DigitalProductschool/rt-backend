from firebase_admin import App
from Backend.DataTypes.Exceptions.IncorrectParameterException import IncorrectParameterException
from Backend.DataTypes.Exceptions.AuthenticationException import AuthenticationException
from ariadne import QueryType
from Backend.database import db
from Backend.DataTypes.Applicant import Applicant
from Backend.DataTypes.Batch import Batch
from Backend.DataTypes.User import User

from flask import jsonify
from Backend.Authentication.verify_token import get_user_context
from Backend.DataTypes.ApplicantList import ApplicantList
from Backend.DataTypes.BatchList import BatchList

batches_details = db.collection('batch-details')
batches = db.collection('batches')
query = QueryType()

@query.field("user")
def resolve_current_user(_, info):
     authentication = get_user_context(info)
     return authentication
   

# TODO This method has to change to query only the information that will be displayed on the applicants List
@query.field("applicants")
def resolve_applicants(_, info, batch_id_list):
    current_user = get_user_context(info)
    # current_user = User(1233, "Magda", "ntmagda393@gmail.com", "photo")
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
                                        None,
                                        application['status']
                                        ))
                except KeyError as err:
                    return IncorrectParameterException(1, "The field" + str(err) + "does not exists in the database document" )
        return ApplicantList(applicants)
    else:
        return AuthenticationException()


@query.field("applicantDetails")
def resolve_applicant_details(_, info, batch_id, applicant_id):
    current_user = get_user_context(info)
    # current_user = User("Magda", "ntmagda393@gmail.com", "photo")

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


@query.field("batches")
def resolve_batches(_, info, batch_id_list):
    current_user = get_user_context(info)
    # current_user = User(1121,"Magda", "ntmagda393@gmail.com", "photo")
    batches = []
    if (current_user):
        if len(batch_id_list) > 0: 
            batches_collection = [doc.to_dict() for doc in batches_details.stream() if doc.to_dict()['batch'] in batch_id_list]
        else: 
            batches_collection = [doc.to_dict() for doc in batches_details.stream()]
        for batch_details in batches_collection:
            try:
                batches.append(Batch(batch_details['batch'],
                                    batch_details['startDate'],
                                    batch_details['endDate'],
                                    batch_details['appStartDate'],
                                    batch_details['appEndDate'],
                                    batch_details['appEndDate-ai'],
                                    batch_details['appEndDate-ixd'],
                                    batch_details['appEndDate-pm'],
                                    batch_details['appEndDate-se']
                                    ))
            except KeyError as err:
                    return IncorrectParameterException(1, "The field" + str(err) + "does not exists in the database document" )
        return BatchList(batches)
    else:
        return AuthenticationException()


@query.field("applicantsFromTrack")
def resolve_applicant_from_track(_, info, batch_id_list, track_list):
    current_user = get_user_context(info)
    # current_user = User("Magda", "ntmagda393@gmail.com", "photo")

    applicants = []

    if (current_user):
        for batch_id in batch_id_list: 
            for track in track_list: 
                batch_doc = batches.document('batch-' + str(batch_id))
                if not batch_doc.get().exists:
                    return IncorrectParameterException(errorMessage='Incorrect batch_id parameter')

                applicationsFromTrack = batch_doc.collection('applications').where('track', '==', track).stream()

                for doc in applicationsFromTrack:
                    application = doc.to_dict()
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
                                                    None,
                                                    application['status']
                                                    ))
                    except KeyError as err:
                        return IncorrectParameterException(1, "The field" + str(err) + "does not exists in the database document" )

        return ApplicantList(applicants)
    else:
        return AuthenticationException(404, "User does not have permissions")


@query.field("applicantsFromStatus")
def resolve_applicant_from_status(_, info, batch_id_list, status_list):
    current_user = get_user_context(info)
    # current_user = User("Magda", "ntmagda393@gmail.com", "photo")
    # to be refactored
    applicants = []

    if (current_user):
        for batch_id in batch_id_list: 
            for status in status_list: 
                batch_doc = batches.document('batch-' + str(batch_id))
                if not batch_doc.get().exists:
                    return IncorrectParameterException(errorMessage='Incorrect batch_id parameter')

                applicationsFromStatus = batch_doc.collection('applications').where('status', '==', status).stream()

                for doc in applicationsFromStatus:
                    application = doc.to_dict()
                    print(application['acceptanceFormData'])
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
                                                    application['acceptanceFormData'],
                                                    application['status']
                                                    ))
                    except KeyError as err:
                        return IncorrectParameterException(1, "The field" + str(err) + "does not exists in the database document" )

        return ApplicantList(applicants)
    else:
        return AuthenticationException(404, "User does not have permissions")

@query.field("applicantsByStatus")
def resolve_applicants_by_status(_, info, batch_id_list, track_list, status_list):
    result = resolve_applicant_from_track(_, info, batch_id_list, track_list)
    if isinstance(result, ApplicantList):
        applicants = result.list
        applicants_by_status = [applicant for applicant in applicants if applicant.status in status_list]
        return ApplicantList(applicants_by_status)
    else: 
        return resolve_applicant_from_track(_, info, batch_id_list, track_list)
