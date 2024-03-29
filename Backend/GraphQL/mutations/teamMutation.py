from Backend.DataTypes.Team import Team
from Backend.DataTypes.Status import Status
from Backend.GraphQL.shared import mutation
from graphql import GraphQLError
from Backend.GraphQL.mutations.emailMutation import mutation_email
from google.cloud import storage
import datetime
from Backend.repositories.team.FirestoreTeamRepository import FirestoreTeamRepository
from Backend.database import db
from Backend.GraphQL.shared import mutation, get_team_document


@mutation.field("addTeam")
def add_team(_, info, name, batch, members, companies):
        teamsRepository = FirestoreTeamRepository(db)
        t = Team(_, name, batch, members, companies)
        status = teamsRepository.add(t, batch)
        return status


@mutation.field("editTeam")
def edit_team(_, info, batch, team_id, updated_data):
        team, _ = get_team_document(batch, team_id)
        team.update(updated_data)
        return Status(0, 'Team was succesfully edited')
