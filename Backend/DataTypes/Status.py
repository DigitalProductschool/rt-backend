import enum

########### STATUS #########
# NEW - the applicant just applied
# Promising Sent - the email that the application is promising is sent
# Challenge Sent - the challenge was sent to applicant
# Q&ASent - the q&a link was sent
# Invitation Sent - invitation link to 1-1 sent
# Interview Scheduled - interview was scheduled
# Interview Done - interview was done
# Accepted - applicant accepted
# Document Sent - applicant received the documents
# Rejected - applicant rejected
# Waiting List Sent - the applicant is in waiting list


class Status():
    def __init__(self, statusCode, message):
        self.code = statusCode
        self.message = message
