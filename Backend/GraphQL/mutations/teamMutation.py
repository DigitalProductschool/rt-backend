from Backend.DataTypes.Team import Team
from Backend.DataTypes.Status import Status
from Backend.GraphQL.shared import mutation
from graphql import GraphQLError
from Backend.GraphQL.mutations.emailMutation import mutation_email
from google.cloud import storage
import datetime
from Backend.repositories.team.FirestoreTeamRepository import FirestoreTeamRepository
from Backend.database import db


@mutation.field("addTeam")
def add_team(_, info, name, batch, members, companies):
        teamsRepository = FirestoreTeamRepository(db)
        t = Team(_, name, batch, members, companies)
        status = teamsRepository.add(t, batch)
        return status