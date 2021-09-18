# Recruitment Backend

## Local usage
### Get firebase credentials
- Create a service account in Google Cloud Platform with Secret Manager Admin permissions. 
- Download json file with the service account key as json file.
- Create .env file based on .env.example
   - Set the GOOGLE_APPLICATION_CREDENTIALS environment variable inside of the .env file pointing to the json in your filesystem 
   - Set the FLASK_APP variable to name of your application (app.py)
   - Specify the host and port in the .env file (default is: 127.0.0.1:5000)

Note: It is important to install python-dotenv library - when installed it will automatically pull the enviornment variables from the .env file 

### Run the app
```
python run.py
```

### Usage of graphql API
* Go to the server /graphql endpoint 
* Insert the query in the following form with desired parameters:


### Dependencies 
* All python packages listed in requirements.txt should be installed.
* In addition the library wkhtmltopdf is required. Can be installed with brew or if project is fired up with the docker-compose the wkhtmltopdf will be installed in the docker image itself. 

## Queries

### Current User
```
query {
    user {
      uid
      name
      email
      photo
    }
  }
```

### Applicants from Batch 
```
query {
  applicants(batch_id_list: [15] ) {
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
```

### Applicant details
```
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
```

### Applicants from Track
Query applicants across multiple batches and multiple tracks
```
query {
  applicantsFromTrack(batch_id_list: [15], track_list: [se, pmc]) {
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
```

### Applicants from Status
Query applicants across multiple batches and multiple statuses
```
 query {
  applicantsFromStatus(batch_id_list: [15], status_list: ["Documents Sent"]) {
	... on ApplicantList{
	  list {
      name
      track
      batch
      acceptanceFormData {
          location
          streetNumber
          addressSuffix
          postcode
          city
          country
          accountHolder
          bankName
          iban
          bic
          shirtSize
          shirtStyle
          foodIntolerances
      }
    }
	}
	... on Exception{
		message
	}
    }
  }
```

### Batches
To get information about the batch with batch_id.
If list is empty - all batches will be returned. If wrong batch number provided - no infomation will be returned. 
```
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
```

## Mutations 
### Rate applicant

```
  mutation {
  rate(batch_id: 15, applicant_id: "4KHMCajcFloiX2sSOUPE", score: 4) {
     ... on Status {
      code
      message
    }
    ... on Exception{
        message
    }
}
}
```

### Send Email

```
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
```

### Create Comment

```
 mutation {
  createComment( batch_id: 15, applicant_id:"SYKh3tjEUpcgCoI9ennO", comment_body: "bela testing") {
     ... on Status {
      code
      message
    }
    ... on Exception{
        message
    }
}
}
```

### Edit Comment

```
 mutation {
  editComment( batch_id: 15, applicant_id:"SYKh3tjEUpcgCoI9ennO",comment_body: "bela again testing", comment_id: "y6wNHyjEAskHCZpzCQpY") {
     ... on Status {
      code
      message
    }
    ... on Exception{
        message
    }
}
}
```

### Delete Comment

```
 mutation {
  deleteComment( batch_id: 15, applicant_id:"SYKh3tjEUpcgCoI9ennO",comment_id: "y6wNHyjEAskHCZpzCQpY") {
     ... on Status {
      code
      message
    }
    ... on Exception{
        message
    }
}
}
```

### Send Acceptance Form

```
mutation{
    saveForm(batch_id: 15, applicant_id: "SYKh3tjEUpcgCoI9ennO", location: "Munich", streetNumber: "Feilitzstrasse", addressSuffix: "-", postcode: "80802", city: "Munich", country: "Germany", accountHolder: "Bela Sinoimeri", bankName: "N26", iban: "12345678", bic: "242426", shirtSize:"M", shirtStyle: "F", foodIntolerances: "none") {
     ...on Status {
        code
        message
      }
    ...on Exception{
        message
      }
    }
}
```