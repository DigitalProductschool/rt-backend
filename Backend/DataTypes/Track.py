from aenum import Enum
from Backend.DataTypes.CoreTeamMember import CoreTeamMember

class Track(Enum):
     SE = 1
     IxD = 2
     PM = 3
     PMC =4
     AI = 5
     AC = 6
     
     @classmethod
     def _missing_name_(cls, name):
        for member in cls:
            if member.name.lower() == name.lower():
                return member

class TrackDetails():
    def __init__(self, track_handle):
        if (track_handle == Track.SE):
            self.handle = 'se'
            self.name = "Software Engineer"
            self.coreTeam =  [CoreTeamMember("Daniel", "https://calendly.com/daniel-dps/dps-interview"),
                              CoreTeamMember("Bela", "https://calendly.com/bela-sinoimeri/dps-interview")]
            self.challengeLink = ["https://dps-challenge-front.netlify.app/contactsapp",
                            "https://dps-challenge-front.netlify.app/bookfinderapp",
                            "https://dps-challenge-front.netlify.app/recipeapp"]
            self.qaLink = "https://calendly.com/digital-product-school-team/q-a"
            
        elif (track_handle == Track.PM):
            self.handle = 'pm'
            self.name = "Product Manager"
            self.coreTeam = [{"name": "Steffen", "calendly": "https://calendly.com/kastner/30min"}]
            self.challengeLink = None
            self.qaLink = None

        elif (track_handle == Track.IxD):
            self.handle = 'IxD'
            self.name = "Interaction Designer"
            self.coreTeam = [{"name": "Marcus", "calendly": None}]
            self.challengeLink = None
            self.qaLink = None

        elif (track_handle == Track.PMC):
            self.handle = 'pmc'
            self.name = "Product Marketing & Communications Manager"
            self.coreTeam = [{"name": "Bastian", "calendly": "https://calendly.com/bastian-rieder/interview-pmc"}]
            self.challengeLink = None
            self.qaLink = None

        elif (track_handle == Track.AI):
            self.handle = 'ai'
            self.name = "AI Engineer"
            self.coreTeam = [{"name": "Afsaneh", "calendly": "https://calendly.com/asaei/interview-dps-ai-track"}]
            self.challengeLink = ["https://dps-challenge-front.netlify.app/opendataportal",
                            "https://dps-challenge-front.netlify.app/vertexAI"]
            self.qaLink = "https://calendly.com/asaei/group-interview-and-q-a-dps-ai-track"      

        elif (track_handle == Track.AC):
            self.handle = 'ac'
            self.name = "Agile Team Coach"
            self.coreTeam = [{"name": "Tobias", "calendly": "https://calendly.com/dps-tobias-kalkowsky/dps-agile-coaching-track-interview"}]
            self.challengeLink = None
            self.qaLink = "https://calendly.com/dps-tobias-kalkowsky/dps-agile-coaching-track-q-a"