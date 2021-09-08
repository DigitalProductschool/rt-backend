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


### dependencies 
all python packages listed in requirements.txt should be installed.
In addition the library wkhtmltopdf is required. 
can be installed with brew. 
Or if project is fired up with the docker-compose the wkhtmltopdf will be installes in the docker image itself. 


    
query {
  applicants(batch_id_list: [13] ) {
	... on ApplicantList{
		list {
      name
      track
      batch
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


There is a possibility to query applicants across multiple batches and multiple tracks:

query {
  applicantsFromTrack(batch_id_list: [14, 13], track_list: [se, pm]) {
	... on ApplicantList{
		list {
      name
      track
      batch
    }
	}
	... on Exception{
		message
	}
    }
  }

There is a possibility to query applicants across multiple batches and multiple tracks and also filter via Status:

query {
  applicantsByStatus(batch_id_list: [13,14], track_list: [se, pm], status_list: ["PRETTY COOL", "NEUTRAL"]) {
	... on ApplicantList{
		list {
      name
      track
      batch
      status
    }
	}
	... on Exception{
		message
	}
    }
  }



To get information about the batch with batch_id.
If list is empty - all batches will be returned. If wrong batch number provided - no infomation will be returned. 

query {
  batches(batch_id_list: [15]) {
    ... on BatchList{
				list {
          startDate
          batch
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

The mutation to send email (with or without documents dependent on the email_type):
mutation {
  sendEmail(applicant_id: "jru16lzWvqxHiuakWN0q", email_type: "sendDocuments", applicant_name:"Magda", applicant_email: "ntmagda93@gmail.com", track:se, batch_id:13) {
     ... on Status {
      code
      message
    }
    ... on Exception{
      code
      message
        
    }
}
}
}