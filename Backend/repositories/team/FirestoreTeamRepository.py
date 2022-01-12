from Backend.repositories.team.AbstractTeamRepository import AbstractTeamRepository
from Backend.DataTypes.Team import Team
from Backend.DataTypes.TeamList import TeamList
from Backend.GraphQL.shared import incorrect_parameter


class FirestoreTeamRepository:

    def __init__(self, db):
        self.batches = db.collection("batches")

    def list(self, reference_list) -> TeamList:
        if reference_list is not None and len(reference_list) > 0:
            teams_list = []
            for ref in reference_list:
                if ref is not None: 
                    batch_doc = self.batches.document('batch-' + str(ref))
                    incorrect_parameter(batch_doc)
                    teams = batch_doc.collection('teams')
                    teams_list += [doc.to_dict() for doc in teams.stream()]
            return TeamList.from_dict(teams_list)
