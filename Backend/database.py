import json
from google.cloud import secretmanager
from firebase_admin import credentials, firestore, initialize_app
import os

# retrieve secrets from Google Cloud Secret Manager
def access_secret_version(secret_id, version_id="latest"):
    # Create the Secret Manager client.
    client = secretmanager.SecretManagerServiceClient()

    # Build the resource name of the secret version.
    name = f"projects/unternehmertum-recruiting-tool/secrets/{secret_id}/versions/1"

    # Access the secret version.
    response = client.access_secret_version(name=name)

    # Return the decoded payload.
    return response.payload.data.decode('UTF-8')


# Initialize Firestore DB
database_config = os.environ.get('SERVICE_ACCOUNT', 'firebase-staging-serviceaccount')
firebase_json = json.loads(access_secret_version(database_config))
cred = credentials.Certificate(firebase_json)
default_app = initialize_app(cred)
db = firestore.client() 
