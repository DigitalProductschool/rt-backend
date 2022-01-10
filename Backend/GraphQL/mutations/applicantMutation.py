from Backend.DataTypes.Emails.Email import Email
from Backend.DataTypes.Status import Status
from Backend.GraphQL.shared import mutation, get_applicant_document, get_batch_document, batches, upload_to_bucket
from graphql import GraphQLError
from Backend.GraphQL.mutations.emailMutation import mutation_email
from google.cloud import storage
import datetime

@mutation.field("addApplicant")
def add_applicant(_, info, name, batch, track, email, cv, scholarship, coverLetter, source, gender, program):
        document = batches.document('batch-' + str(batch)).collection("applicants").document()
        blob_time = int(datetime.datetime.today().timestamp())
        blob_name = "batch-" + str(batch)+"/applications/"+ name +"/"+ email + "/" + str(blob_time) + "_" 
        cvBucket, cvName = upload_to_bucket(blob_name, cv)
        coverBucket, coverName = upload_to_bucket(blob_name, coverLetter)
        applicantData = {
            "id": document.id,
            "batch": str(batch),
            "name": name, 
            "track": track, 
            "email": email, 
            "consent": "true",
            "cv": { 
                "bucket": cvBucket, 
                "name": cvName
                },
            "scholarship": scholarship,
            "coverLetter": { 
                "bucket": coverBucket, 
                "name": coverName
                },
            "source": source, 
            "gender": gender, 
            "status": "NEW",
            "program": program, 
        }
        batches.document('batch-' + str(batch)).collection("applications").document(document.id).set(applicantData)
        return Status(0, 'Applicant was succesfully added')

@mutation.field("editApplicant")
def edit_applicant(_, info, batch_id, applicant_id, updated_data):
        application, _ = get_applicant_document(batch_id, applicant_id)
        application.update(updated_data)
        return Status(0, 'Applicant was succesfully edited')
