import imp
from Backend.DataTypes.Applicant import Applicant

class ApplicantList():
    def __init__(self, applicantList):
        self.list = applicantList



    @classmethod
    def from_dict(cls, tl):
        teams = []
        for team in tl:
            t = Applicant.from_dict(team)
            teams.append(t)
        return ApplicantList(teams)
