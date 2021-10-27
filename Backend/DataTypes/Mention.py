from Backend.DataTypes.User import User


class MentionData(): 
    def __init__(self, applicantId, batchId, commentId):
        self.applicantId = applicantId
        self.batchId = batchId
        self.commentId = commentId

class Mention():
    def __init__(self, id, createdAt, data , mentioner, new = "True"):
        self.id = id
        self.createdAt = createdAt
        self.data = MentionData(data["applicantId"], data["batchId"], data["commentId"])
        self.mentioner =  User(mentioner["uid"], mentioner["name"], None, mentioner["photo"])
        self.new = new
