import abc
from Backend.DataTypes.Batch import Batch
from Backend.DataTypes.BatchList import BatchList


class AbstractBatchRepository(abc.ABC):

    @abc.abstractmethod
    def get(self, reference) -> Batch:
        raise NotImplementedError

    @abc.abstractmethod
    def list(self, reference_list=None) -> BatchList:
        raise NotImplementedError
