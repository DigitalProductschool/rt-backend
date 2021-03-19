
from uuid import uuid4
class Applicant:
   def __init__(self, name, surname):
       self.name = name
       self.surname = surname
       self.id = uuid4()

       
