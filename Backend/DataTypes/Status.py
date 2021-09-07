import enum


########### STATUS #########
# NEW - the applicant did not receive sufficient amount of votes
# NEUTRAL - the applicant is below the threshold
# PRETTY_COOL - the applicant is above the threshold
# ChallengeSent - the challenge was sent to applicant
# Q&ASent - the q&a link was sent
# InvitationSent - invitatin link to 1-1 sent
# Accepted - applicant accepted 
# DocumentSent - applicant received the documents 
# Rejected - applicant rejected


class Status():
    def __init__(self, statusCode, message):
        self.code = statusCode
        self.message = message