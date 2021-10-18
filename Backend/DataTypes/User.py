class User():
    def __init__(self, uid, name, email, photo, role="OWNER"):
        self.uid = uid
        self.name = name
        self.email = email
        self.photo = photo
        self.role = role
