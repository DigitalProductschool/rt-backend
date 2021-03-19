# app.py
# Required imports
import os
from flask import Flask, request, jsonify
from ariadne import graphql_sync, make_executable_schema, gql, load_schema_from_path
from firebase_admin import credentials, firestore, initialize_app
from google.cloud import secretmanager
import json
from ariadne.constants import PLAYGROUND_HTML
from models import query
from flask_cors import CORS


# retrieve secrets from Google Cloud Secret Manager
def access_secret_version(secret_id, version_id="latest"):
    # Create the Secret Manager client.
    client = secretmanager.SecretManagerServiceClient()

    # Build the resource name of the secret version.
    name = f"projects/unternehmertum-recruiting-tool/secrets/{secret_id}/versions/1"

    # Access the secret version.
    response = client.access_secret_version(name=name)

    # Return the decoded payload.
    return json.loads(response.payload.data.decode('UTF-8'))


# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Initialize Firestore DB
firebase_json = access_secret_version("firebase-staging-serviceaccount")
cred = credentials.Certificate(firebase_json)
default_app = initialize_app(cred)
db = firestore.client()
details_ref = db.collection('batch-details')

###################### GRAPHQL API #######################

type_defs = gql(load_schema_from_path("./schema.graphql"))
schema = make_executable_schema(type_defs, query)



@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
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


#################### REST API #########################

@app.route('/batches/list', methods=['GET'])
def read():
    """
        read() : Fetches documents from Firestore collection as JSON.
        batch_detail : Return document that matches query ID.
        all_batches : Return all documents.
    """
    try:
        # Check if ID was passed to URL query
        batch_id = request.args.get('id')
        if batch_id:
            batch = details_ref.document(batch_id).get()
            return jsonify(batch.to_dict()), 200
        else:
            all_batches = [doc.to_dict() for doc in details_ref.stream()]
            return jsonify(all_batches), 200
    except Exception as e:
        return f"An Error Occured: {e}"


@app.route('/batches/applicants', methods=['GET'])
def read_applicants_list():
    batches = db.collection('batches')
    participants_details=''
    try:
        # Check if ID was passed to URL query
        batch_id = request.args.get('id')
        if batch_id:
            applications = batches.document('batch-'+str(batch_id)).collection('applications')
            participants_details = [doc.to_dict() for doc in applications.stream()]
            return jsonify(participants_details), 200
        else:
            return "Please specify the batch", 200
    except Exception as e:
        return f"An Error Occurred: {e}"

