from Backend.repositories.AbstractRepository import AbstractRepository
from Backend.DataTypes.Applicant import Applicant
from Backend.DataTypes.ApplicantList import ApplicantList
from Backend.GraphQL.shared import incorrect_parameter, create_applicant
from Backend.DataTypes.Status import Status
from graphql import GraphQLError


class FirestoreApplicantRepository(AbstractRepository):

    def __init__(self, db):
        self.batches = db.collection("batches")

    def get_all_from_batch_list(self, batch_id_list) -> ApplicantList:
        if batch_id_list is not None and len(batch_id_list) > 0:
            applicants = []
            for ref in batch_id_list:
                batch_doc = self.batches.document('batch-' + str(ref))
                incorrect_parameter(batch_doc)
                applications = batch_doc.collection('applications')
                applications = [doc.to_dict() for doc in applications.stream()]
                for application in applications:
                    applicants.append(create_applicant(application))
        return ApplicantList(applicants)

    def get_all_from_batch(self, batch_id):
        pass
    def get_from_batch_by_id(self, batch_id, id):
        pass 
    def get_from_batch_by_id_list(self, batch_id, id_list): 
        pass 