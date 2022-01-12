from Backend.database import db
from ariadne import MutationType
from ariadne import QueryType
from graphql import GraphQLError
from Backend.DataTypes.Applicant import Applicant, PMCApplicant
from Backend.DataTypes.Track import Track
from Backend.DataTypes.Status import Status
from Backend.DataTypes.Program import Program
from functools import lru_cache
from firebase_admin import storage
from Backend.config import config

batch_details = db.collection('batch-details')
batches = db.collection('batches')
users = db.collection('users')
programs = db.collection('programs')
companies =  db.collection('companies')
mutation = MutationType()
query = QueryType()


def incorrect_parameter(doc):
    if not doc.get().exists:
        raise GraphQLError(message='Incorrect parameter')

def upload_to_bucket(blob_name, file):
    bucket_name = config.BUCKET_NAME
    bucket = storage.bucket(bucket_name)
    blob = bucket.blob(blob_name + file.filename)
    blob.upload_from_file(file,content_type='application/pdf')
    return bucket_name, blob_name + file.filename

def get_batch_document(batch_id):
    batch_doc = batches.document('batch-' + str(batch_id))
    incorrect_parameter(batch_doc)
    return batch_doc


def get_applicant_document(batch_id, applicant_id):
    batch_doc = get_batch_document(batch_id)
    applications = batch_doc.collection('applications')
    application_doc = applications.document(str(applicant_id))
    incorrect_parameter(application_doc)
    application_details = application_doc.get().to_dict()
    return application_doc, application_details

def get_team_document(batch_id, team_id):
    batch_doc = get_batch_document(batch_id)
    teams = batch_doc.collection('teams')
    team_doc = teams.document(str(team_id))
    incorrect_parameter(team_doc)
    team_details = team_doc.get().to_dict()
    return team_doc, team_details

def get_comment_document(batch_id, applicant_id, document_id = None):
    applicant_doc, _ = get_applicant_document(batch_id, applicant_id)
    comment_doc = applicant_doc.collection('comments').document(document_id)
    return comment_doc

def get_user_document(user_id):
    user_doc = users.document(user_id)
    incorrect_parameter(user_doc)
    user_details = user_doc.get().to_dict()
    return user_doc, user_details

@lru_cache()
def get_program_document(program_id):
    program_doc = programs.document(program_id)
    incorrect_parameter(program_doc)
    program_details = program_doc.get().to_dict()
    return program_details

def get_current_user(info):
    user = info.context.get('user')
    if not user: 
         raise GraphQLError(message="User does not have permissions")
    return user


def update_status(application, status):
        application.update({'status': status})
        return Status(0, 'Status was updated succesfuly')


def create_applicant(applicant, generate=True):
    program_details = get_program_document(applicant['program'])
    try:
        if Track[applicant["track"]].__str__() == "PMC":
            return PMCApplicant(applicant['id'],
                                applicant['name'],
                                applicant['batch'],
                                applicant['track'],
                                applicant['email'],
                                applicant['consent'],
                                applicant['cv'],
                                applicant['scholarship'],
                                applicant['coverLetter'],
                                applicant['source'],
                                applicant['gender'],
                                applicant['acceptanceFormData'] if 'acceptanceFormData' in applicant else None,
                                applicant['project'] if 'project' in applicant else None,
                                applicant['strengths'] if 'strengths' in applicant else None,
                                applicant['status'], 
                                program_details
                                )
        else:
            return Applicant(applicant['id'],
                             applicant['name'],
                             applicant['batch'],
                             applicant['track'],
                             applicant['email'],
                             applicant['consent'],
                             applicant['cv'],
                             applicant['scholarship'],
                             applicant['coverLetter'],
                             applicant['source'],
                             applicant['gender'],
                             applicant['acceptanceFormData'] if 'acceptanceFormData' in applicant else None,
                             applicant['status'], 
                             program_details,
                             generate
                             )
    except KeyError as err:
        return GraphQLError(message="The field" + str(err) + "does not exists in the database document")
