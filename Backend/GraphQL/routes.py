import os
import json
from flask import Flask, request, jsonify, Blueprint
from ariadne import graphql_sync, make_executable_schema, gql, load_schema_from_path, upload_scalar, combine_multipart_data
from ariadne.constants import PLAYGROUND_HTML
from Backend.GraphQL.mutations.mentionMutation import mutation
from Backend.GraphQL.mutations.commentMutation import mutation
from Backend.GraphQL.mutations.statusMutation import mutation
from Backend.GraphQL.mutations.emailMutation import mutation
from Backend.GraphQL.mutations.formMutation import mutation
from Backend.GraphQL.mutations.rateMutation import mutation
from Backend.GraphQL.mutations.applicantMutation import mutation
from Backend.GraphQL.mutations.teamMutation import mutation
from Backend.GraphQL.queries.applicantDetails import query
from Backend.GraphQL.queries.applicants import query
from Backend.GraphQL.queries.batches import query
from Backend.GraphQL.queries.teams import query
from Backend.GraphQL.queries.applicantsFromTrack import query
from Backend.GraphQL.queries.applicantsFromStatus import query
from Backend.GraphQL.queries.applicantsFromTrackAndStatus import query
from Backend.GraphQL.queries.applicants import query
from Backend.GraphQL.queries.currentUser import query
from Backend.GraphQL.queries.users import query
from Backend.GraphQL.queries.companies import query
from Backend.GraphQL.queries.programs import query
from Backend.GraphQL.queries.programDetails import query
from Backend.GraphQL.queries.userMentions import query
from Backend.GraphQL.queries.applicantComments import query
from Backend.GraphQL.unionResolvers import ApplicantsQueryResult, CommentsQueryResult, ApplicantDetailsQueryResult, BatchesQueryResult, TeamsQueryResult, UserQueryResult, UsersQueryResult, UserMentionsQueryResult, ProgramsQueryResult, ProgramDetailsQueryResult, CompaniesQueryResult, MutationResult
from Backend.GraphQL.shared import query
from Backend.GraphQL.scalarType import datetime_scalar
from flask_cors import CORS
from Backend.database import db
from datetime import timedelta
from flask import current_app as app
from Backend.UserManagement.context import get_user_context
from graphql import default_field_resolver, GraphQLError
from flask import request
from Backend.GraphQL.directives import IsAuthenticatedDirective
from ariadne import format_error

graphql = Blueprint('graphql', __name__)
batch_details = db.collection('batch-details')

###################### GRAPHQL API #######################

type_defs = gql(load_schema_from_path("Backend/GraphQL/schema.graphql"))
schema = make_executable_schema(type_defs, [query, 
                                            mutation,
                                            datetime_scalar,
                                            ApplicantsQueryResult, 
                                            CommentsQueryResult, 
                                            ApplicantDetailsQueryResult, 
                                            BatchesQueryResult, 
                                            UserQueryResult, 
                                            UsersQueryResult, 
                                            UserMentionsQueryResult, 
                                            ProgramsQueryResult, 
                                            ProgramDetailsQueryResult, 
                                            TeamsQueryResult, 
                                            CompaniesQueryResult,
                                            MutationResult, 
                                            upload_scalar], 
                                            directives={"isAuthenticated": IsAuthenticatedDirective})


@graphql.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@graphql.route("/graphql", methods=["POST"])
def graphql_server():
    if request.content_type.startswith("multipart/form-data"):
        data = combine_multipart_data(
            json.loads(request.form.get("operations")),
            json.loads(request.form.get("map")),
            dict(request.files)
        )
    else:
        data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=get_user_context(),
        debug= app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code

