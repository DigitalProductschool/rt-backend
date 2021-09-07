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
  applicants(batch_id: 13) {
	... on ApplicantList{
		list {
      name
      track
    }
	}
	... on Exception{
		message
	}
    }
  }


  
query {
  applicantDetails(batch_id: 13, applicant_id: "jru16lzWvqxHiuakWN0q") {
    ... on Applicant{
      name
      email
      batch
      track
      scholarship
      gender
    }
    ... on Exception{
        message
    }
    }
  }


To get information about the batch with batch_id: ( if batch_id == null all batches will be listed)

query {
  batches(batch_id: null) {
    ... on BatchList{
				list {
          startDate
        }
    }
    ... on Exception{
        message
    }
    }
  }


The mutation example to rate an applicant:

  mutation {
  rate(batch_id: 13, applicant_id: "jru16lzWvqxHiuakWN0q", score: 4) {
     ... on Status {
      code
      message
    }
    ... on Exception{
        message
    }
}
}

The mutation to send email:

 mutation {
  sendEmail(email_type: "sendChallenge", applicant_name: "Bela", applicant_email: "belasinoimeri@gmail.com", track: se, batch_id: 15, applicant_id:"IX12MMJC2ZRghqyuw1uS") {
     ... on Status {
      code
      message
    }
    ... on Exception{
        message
    }
}
}


The mutation to send email with documents attached:

 mutation {
  sendEmailDocuments(applicant_name: "Bela", applicant_email: "belasinoimeri@gmail.com", track: se, batch_id: 15, applicant_id:"IX12MMJC2ZRghqyuw1uS") {
     ... on Status {
      code
      message
    }
    ... on Exception{
        message
    }
}
}