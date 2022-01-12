from Backend.repositories.team.AbstractTeamRepository import AbstractTeamRepository
from Backend.DataTypes.Team import Team
from Backend.DataTypes.TeamList import TeamList
from Backend.GraphQL.shared import incorrect_parameter
from Backend.DataTypes.Status import Status
from graphql import GraphQLError


class FirestoreTeamRepository:

    def __init__(self, db):
        self.batches = db.collection("batches")

    def list(self, reference_list) -> TeamList:
        if reference_list is not None and len(reference_list) > 0:
            teams_list = []
            for ref in reference_list:
                batch_doc = self.batches.document('batch-' + str(ref))
                incorrect_parameter(batch_doc)
                teams = batch_doc.collection('teams')
                teams_list += [doc.to_dict() for doc in teams.stream()]
            return TeamList.from_dict(teams_list)

    def add(self, t, batch) -> Status: 
        batch_doc = self.batches.document('batch-' + str(batch))
        incorrect_parameter(batch_doc)
        document = batch_doc.collection("teams").document()
        t.id = document.id
        self.batches.document('batch-' + str(batch)).collection("teams").document(document.id).set(t.__dict__)
        return Status(0, "Team was succesfully added")

    
        


    