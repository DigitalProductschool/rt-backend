from Backend.DataTypes.Emails.Email import Email
from Backend.DataTypes.Status import Status
from Backend.GraphQL.shared import mutation, get_applicant_document, get_batch_document, batches, upload_to_bucket
from graphql import GraphQLError
from Backend.GraphQL.mutations.emailMutation import mutation_email
from google.cloud import storage
import datetime

@mutation.field("addApplicant")
def add_applicant(_, info, name, batch, track, email, cv, scholarship, coverLetter, source, gender, status, program):
        document = batches.document('batch-' + str(batch)).collection("applicants").document()
        blob_time = int(datetime.datetime.today().timestamp())
        blob_name = "batch-" + str(batch)+"/applications/"+ name +"/"+ email + "/" + str(blob_time) + "_" 
        cvBucket, cvName = upload_to_bucket(blob_name, cv)
        coverBucket, coverName = upload_to_bucket(blob_name, coverLetter)
        applicantData = {
            "id": document.id,
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
def edit_applicant(_, info, name, batch, track, email, consent, cv, scholarship, coverLetter, source, gender, status, program):
        uid = batches.document('batch-' + str(batch_id)).collection("applicants").document().getId()
        applicantData = {
            "id": uid,
            "name": name, 
            "track": track, 
            "email": email, 
            "consent": "true",
            "cv": True, 
            "scholarship": scholarship,
            "coverLetter": True, 
            "source": source, 
            "gender": gender, 
            "status": "NEW",
            "program": program, 
        }
        batches.document('batch-' + str(batch_id)).collection("applicants").document(uid).set(applicantData)
        return Status(0, 'Applicant was succesfully added')
