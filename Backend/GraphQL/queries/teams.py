
from Backend.GraphQL.shared import query
from Backend.repositories.team.FirestoreTeamRepository import FirestoreTeamRepository
from graphql import GraphQLError
from Backend.database import db


@query.field("teams")
def resolve_teams(_, info, batch_id_list):
    teamsRepository = FirestoreTeamRepository(db)
    res = teamsRepository.get_all_from_batch_list(batch_id_list)
    if not res:
        raise GraphQLError(message="Incorrect parameter")
    return res