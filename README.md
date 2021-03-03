# Recruitment backend

## local usage
### get firebase credentials
Create a service account in Google Cloud Platform with Secret Manager Admin permissions. 
Download json file with the service account key as json file.
create .env file based on .env.example
Set the GOOGLE_APPLICATION_CREDENTIALS environment variable inside of the .env file pointing to the json in your filesystem 

### run the app
python app.py