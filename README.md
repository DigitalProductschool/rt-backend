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
    ... on User{
      uid
      name
      email
      photo
    }
    ... on Exception{
		message
	}
    }
  }
```
### Users
```
query {
    users {
    ... on UserList{
	  list {
      uid
      name
      email
      photo
    }
	}
	... on Exception{
		message
	}
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
      track {
        handle
      }
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
  applicantDetails(batch_id: 15, applicant_id: "4KHMCajcFloiX2sSOUPE") {
    ... on Applicant{
      id
      name
      batch
      track {
        handle
        name
        coreTeam {
          name
          calendly
        }
        qaLink
      }
      email
      consent
      cv {
          name
          bucket
      }
      scholarship
      coverLetter {
          name 
          bucket
      }
      source
      gender
      acceptanceFormData {
          location
      }
      project
      strengths
      status
    }
    ... on Exception{
        message
    }
    }
  }
```

### Applicant comments 
```
query {
  applicantComments(batch_id: 15, applicant_id: "4KHMCajcFloiX2sSOUPE") {
    ... on CommentList{
        list{
       id
       body
       createdAt
       updatedAt
       user {
        name
        photo
        email
        uid
    }
        }
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
  applicantsFromTrack(batch_id_list: [15], track_list: [se, pmc, pm]) {
	... on ApplicantList{
		list {
      name
      track {
        handle
      }
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
  applicantsFromStatus(batch_id_list: [15], status_list: ["Rejected"]) {
	... on ApplicantList{
	  list {
      name
      track {
        handle
      }
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
### Applicants from Track & Status
Query applicants across multiple batches and multiple tracks and multiple statuses
```
query {
  applicantsFromTrackAndStatus(batch_id_list: [15], track_list: [se, pmc, pm], status_list:["NEW"]) {
	... on ApplicantList{
		list {
      name
      track {
        handle
      }
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

## Mentions for current user
```
query{
    userMentions {
    ... on MentionList{
		  list {
          mentioner {
          name
          }
          createdAt
          data{
          commentId
          applicantId
          batchId
          }
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
  sendEmail(applicant_id: "4KHMCajcFloiX2sSOUPE", email_type: "sendFormConfirmation", batch_id:15) {
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
  createComment( batch_id: 15, applicant_id:"4KHMCajcFloiX2sSOUPE", comment_body: "bela testing") {
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
  editComment( batch_id: 15, applicant_id:"4KHMCajcFloiX2sSOUPE",comment_body: "bela again testing", comment_id: "y6wNHyjEAskHCZpzCQpY") {
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
  deleteComment( batch_id: 15, applicant_id:"4KHMCajcFloiX2sSOUPE",comment_id: "y6wNHyjEAskHCZpzCQpY") {
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
    saveForm(batch_id: 15, applicant_id: "4KHMCajcFloiX2sSOUPE", location: "Munich", streetNumber: "Feilitzstrasse", addressSuffix: "-", postcode: "80802", city: "Munich", country: "Germany", accountHolder: "Bela Sinoimeri", bankName: "N26", iban: "12345678", bic: "242426", shirtSize:"M", shirtStyle: "F", foodIntolerances: "none") {
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
### Change status

```
mutation{
    updateStatus(applicant_id: "4KHMCajcFloiX2sSOUPE", batch_id: 15, status: "none") {
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

## Create mention
```
mutation{
    createMention(batch_id: 15, applicant_id: "4KHMCajcFloiX2sSOUPE", comment_id:"CuW6VkL57rwygUqsV9VK", mentioned_id: "CXIKt8TItcc9rQU7DeiiaYDGBRf2") {
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

## Read mention
```
mutation{
    readMention( mention_id: "bI9u3k6DtDVp0KDxHK2k") {
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
