from Backend.repositories.batch.AbstractBatchRepository import AbstractBatchRepository
from Backend.DataTypes.Batch import Batch
from Backend.DataTypes.BatchList import BatchList


class InMemoryBatchRepository(AbstractBatchRepository):
    def __init__(self):
        self.batchList: BatchList = self.__generate_batch_list()

    def get(self, reference: int) -> Batch:
        try:
            return next(obj for obj in self.batchList.list if obj.batch == reference)
        except StopIteration as exc:
            raise KeyError(reference) from exc

    def list(self, reference_list=None) -> BatchList:
        return self.batchList

    @staticmethod
    def __generate_batch_list() -> BatchList:
        b1 = Batch(15,
                   "2022-01-16T23:00:00+00:00",
                   "2022-04-08T21:59:59+00:00",
                   "2021-05-31T22:00:00+00:00",
                   "2021-10-20T21:59:59+00:00",
                   "2021-10-20T21:59:59+00:00",
                   "2021-10-20T21:59:59+00:00",
                   "2021-10-20T21:59:59+00:00",
                   "2021-10-20T21:59:59+00:00")
        b2 = Batch(16,
                   "2023-01-16T23:00:00+00:00",
                   "2023-04-08T21:59:59+00:00",
                   "2022-05-31T22:00:00+00:00",
                   "2022-10-20T21:59:59+00:00",
                   "2022-10-20T21:59:59+00:00",
                   "2022-10-20T21:59:59+00:00",
                   "2022-10-20T21:59:59+00:00",
                   "2022-10-20T21:59:59+00:00")
        return BatchList([b1, b2])
