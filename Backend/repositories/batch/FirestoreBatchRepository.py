from Backend.repositories.AbstractRepository import AbstractRepository
from Backend.DataTypes.Batch import Batch
from Backend.DataTypes.BatchList import BatchList


class FirestoreBatchRepository(AbstractRepository):

    def __init__(self, db):
        self.batch_details = db.collection("batch-details")

    def get(self, reference: int) -> Batch:
        pass

    def list(self, reference_list=None) -> BatchList:
        if reference_list is not None and len(reference_list) > 0:
            batches_collection = [doc.to_dict() for doc in self.batch_details.stream() if
                                  doc.to_dict()['batch'] in reference_list]
        else:
            batches_collection = [doc.to_dict() for doc in self.batch_details.stream()]
        return BatchList.from_dict(batches_collection)
