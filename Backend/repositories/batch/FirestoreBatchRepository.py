from Backend.repositories.batch.AbstractBatchRepository import AbstractBatchRepository
from Backend.DataTypes.Batch import Batch
from Backend.DataTypes.BatchList import BatchList
from Backend.GraphQL.shared import query, batch_details


class FirestoreBatchRepository(AbstractBatchRepository):

    def __init__(self):
        pass

    def get(self, reference: int) -> Batch:
        pass

    def list(self, reference_list=None) -> BatchList:
        if len(reference_list) > 0:
            batches_collection = [doc.to_dict() for doc in batch_details.stream() if
                                  doc.to_dict()['batch'] in reference_list]
        else:
            batches_collection = [doc.to_dict() for doc in batch_details.stream()]
        return BatchList.from_dict(batches_collection)