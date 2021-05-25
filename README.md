# Recruitment backend

## local usage
### get firebase credentials
- Create a service account in Google Cloud Platform with Secret Manager Admin permissions. 
- Download json file with the service account key as json file.
- create .env file based on .env.example
   - Set the GOOGLE_APPLICATION_CREDENTIALS environment variable inside of the .env file pointing to the json in your filesystem 
   - Set the FLASK_APP variable to name of your application (app.py)
   - Specify the host and port in the .env file (default is: 127.0.0.1:5000)

Note: It is important to install python-dotenv library - when installed it will automatically pull the enviornment variables from the .env file 

### run the app
python run.py

### usage of graphql API
go to the server /graphql endpoint 
insert the query in the following form with desired parameters:

query {
  applicants(batch_id: 14) {
	... on ApplicantList{
		list {
      name
      track
    }
	}
	... on AuthenticationException{
		message
	}
    }
  }

query {
  applicantDetails(batch_id: 14, applicant_id: "zK7RVAcrNOeEiFWGnmUL") {
    ... on Applicant{
      name
      email
      batch
      track
      scholarship
      gender
    }
    ... on AuthenticationException{
        message
    }
    }
  }