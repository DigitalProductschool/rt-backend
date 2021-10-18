from Backend.DataTypes.Batch import Batch


class BatchList():
    def __init__(self, batchList):
        self.list = batchList

    @classmethod
    def from_dict(cls, bl):
        batches = []
        for batch in bl:
            b = Batch.from_dict(batch)
            batches.append(b)
        return BatchList(batches)

