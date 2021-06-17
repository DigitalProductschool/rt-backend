import enum


########### STATUS #########
# NEW - the applicant did not receive sufficient amount of votes
# NEUTRAL - the applicant is below the threshold
# PRETTY_COOL - the applicant is above the threshold




class Status():
    def __init__(self, statusCode, message):
        self.code = statusCode
        self.message = message