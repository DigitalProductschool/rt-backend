from Backend.DataTypes.User import User


class Comment():
    def __init__(self, id, createdAt, updatedAt, body, user):
        self.id = id
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        self.body = body
        self.user = User(user["uid"], user["name"], None, user["photo"])
