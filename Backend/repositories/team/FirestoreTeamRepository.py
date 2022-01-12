from Backend.repositories.AbstractRepository import AbstractRepository
from Backend.DataTypes.Team import Team
from Backend.DataTypes.TeamList import TeamList
from Backend.GraphQL.shared import incorrect_parameter


class FirestoreTeamRepository(AbstractRepository):

    def __init__(self, db):
        self.batches = db.collection("batches")


    def get(self, reference: int) -> TeamList:
        if reference is not None and reference > 0: 
            batch_doc = self.batches.document('batch-' + str(reference))
            incorrect_parameter(batch_doc)
            teams = batch_doc.collection('teams')
            teams_collection = [doc.to_dict() for doc in teams.stream()]
            return TeamList.from_dict(teams_collection)



    def list(self, reference_list=None) -> TeamList:
        pass
        # if reference_list is not None and len(reference_list) > 0:
          
        #     batches_collection = [doc.to_dict() for doc in self.batches.stream() if
        #                           doc.to_dict()['team'] in reference_list]

            
        # else:
        #     batches_collection = [doc.to_dict() for doc in self.batches.stream()]
        # return TeamList.from_dict(batches_collection)
