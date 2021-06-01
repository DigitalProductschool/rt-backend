import enum


########### STATUS #########
# NEW - the applicant did not receive sufficient amount of votes
# NEUTRAL - the applicant is below the threshold
# PRETTY_COOL - the applicant is above the threshold



class StatusType(enum.Enum):
    NEW = 0
    NEUTRAL = 1
    PRETTY_COOL = 2

class Status():
    def __init__(self, statusType, message):
        self.code = statusType
        self.message = message