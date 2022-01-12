from Backend.DataTypes.Team import Team


class TeamList():
    def __init__(self, teamList):
        self.list = teamList
        
    @classmethod
    def from_dict(cls, tl):
        teams = []
        for team in tl:
            t = Team.from_dict(team)
            teams.append(t)
        return TeamList(teams)
