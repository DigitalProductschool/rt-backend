# app.py
# Required imports
import os
from flask import Flask, request, jsonify, Blueprint
from ariadne import graphql_sync, make_executable_schema, gql, load_schema_from_path
from ariadne.constants import PLAYGROUND_HTML
from Backend.GraphQL.queries import query, ApplicantsQueryResult, BatchesQueryResult
from flask_cors import CORS
from Backend.database import db
from datetime import timedelta
from flask import current_app as app

graphql = Blueprint('graphql', __name__)
batch_details = db.collection('batch-details')

###################### GRAPHQL API #######################

type_defs = gql(load_schema_from_path("Backend/GraphQL/schema.graphql"))
schema = make_executable_schema(type_defs, [query, ApplicantsQueryResult, BatchesQueryResult])


@graphql.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200



@graphql.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code

