import abc
from Backend.DataTypes.Team import Team
from Backend.DataTypes.TeamList import TeamList


class AbstractTeamRepository(abc.ABC):

    ## get list of teams after specyfing batch list 
    @abc.abstractmethod
    def list(self, reference_list) -> TeamList:
        raise NotImplementedError