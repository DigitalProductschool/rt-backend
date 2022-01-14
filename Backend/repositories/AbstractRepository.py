import abc

class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def get_all_from_batch_list(self, batch_id_list):
        raise NotImplementedError

    @abc.abstractmethod
    def get_all_from_batch(self, batch_id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_from_batch_by_id(self, batch_id, id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_from_batch_by_id_list(self, batch_id, id_list):
        raise NotImplementedError