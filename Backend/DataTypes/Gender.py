import enum 

class Gender(enum.Enum):
    
    FEMALE = 1
    MALE = 2 
    UNKNOWN = 3
    
    @staticmethod
    def from_str(label):
        if label == 'female':
            return Gender.FEMALE
        if label == 'male':
            return Gender.MALE
        if label == 'unknown' or 'null':
            return Gender.UNKNOWN
        else:
            raise NotImplementedError

