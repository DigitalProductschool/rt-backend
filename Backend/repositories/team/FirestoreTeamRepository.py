from Backend.repositories.AbstractRepository import AbstractRepository
from Backend.DataTypes.Team import Team
from Backend.DataTypes.TeamList import TeamList
from Backend.GraphQL.shared import incorrect_parameter
from Backend.DataTypes.Status import Status
from graphql import GraphQLError


class FirestoreTeamRepository(AbstractRepository):

    def __init__(self, db):
        self.batches = db.collection("batches")

    def get_all_from_batch_list(self, batch_id_list) -> TeamList:
        if batch_id_list is not None and len(batch_id_list) > 0:
            teams_list = []
            for ref in batch_id_list:
                batch_doc = self.batches.document('batch-' + str(ref))
                incorrect_parameter(batch_doc)
                teams = batch_doc.collection('teams')
                teams_list += [doc.to_dict() for doc in teams.stream()]
            return TeamList.from_dict(teams_list)

    def get_all_from_batch(self, batch_id):
        pass

    def get_from_batch_by_id(self, batch_id, id):
        pass

    def get_from_batch_by_id_list(self, batch_id, id_list):
        pass


    def add(self, t, batch) -> Status: 
        batch_doc = self.batches.document('batch-' + str(batch))
        incorrect_parameter(batch_doc)
        document = batch_doc.collection("teams").document()
        t.id = document.id
        self.batches.document('batch-' + str(batch)).collection("teams").document(document.id).set(t.__dict__)
        return Status(0, "Team was succesfully added")

    
        


    