import  enum 
# for now Track Enum is not used, because track is represetned as a string in the database - maybe we should change that?
class Track(enum.Enum):
    SE = 1
    AI = 2
    PM = 3
    UX = 4
    AC = 5
    PMC = 6

    @staticmethod
    def from_str(label):
        if label == 'se':
            return Track.SE
        if label == 'ai':
            return Track.AI
        if label == 'pm':
            return Track.PM
        if label == 'ixd':
            return Track.UX
        if label == 'ac':          
            return Track.AC
        if label == 'pmc':          
            return Track.PMC
        else:
            raise NotImplementedError
