import abc

class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def get(self, reference):
        raise NotImplementedError

    @abc.abstractmethod
    def list(self, reference_list=None):
        raise NotImplementedError
