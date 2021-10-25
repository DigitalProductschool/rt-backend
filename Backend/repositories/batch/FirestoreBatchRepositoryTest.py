import unittest

from Backend.repositories.batch.FirestoreBatchRepository import FirestoreBatchRepository
from mockfirestore import MockFirestore


class FirestoreBatchRepositoryTest(unittest.TestCase):

    def setUp(self):
        self.db = MockFirestore()

        self.db._data = {'batch-details': {
            '15': {
                'batch': 15,
                'startDate': "2022-01-16T23:00:00+00:00",
                "endDate": "2022-04-08T21:59:59+00:00",
                "appStartDate": "2021-05-31T22:00:00+00:00",
                "appEndDate": "2021-10-20T21:59:59+00:00",
                "appEndDate-ai": "2021-10-20T21:59:59+00:00",
                "appEndDate-ixd": "2021-10-20T21:59:59+00:00",
                "appEndDate-pm": "2021-10-20T21:59:59+00:00",
                "appEndDate-se": "2021-10-20T21:59:59+00:00",
                "appEndDate-pmc": "2021-10-20T21:59:59+00:00",
                "appEndDate-ac": "2021-10-20T21:59:59+00:00"
            },
            '16': {
                'batch': 16,
                'startDate': "2022-01-16T23:00:00+00:00",
                "endDate": "2022-04-08T21:59:59+00:00",
                "appStartDate": "2021-05-31T22:00:00+00:00",
                "appEndDate": "2021-10-20T21:59:59+00:00",
                "appEndDate-ai": "2021-10-20T21:59:59+00:00",
                "appEndDate-ixd": "2021-10-20T21:59:59+00:00",
                "appEndDate-pm": "2021-10-20T21:59:59+00:00",
                "appEndDate-se": "2021-10-20T21:59:59+00:00",
                "appEndDate-pmc": "2021-10-20T21:59:59+00:00",
                "appEndDate-ac": "2021-10-20T21:59:59+00:00"
            },
            '17': {
                'batch': 17,
                'startDate': "2022-01-16T23:00:00+00:00",
                "endDate": "2022-04-08T21:59:59+00:00",
                "appStartDate": "2021-05-31T22:00:00+00:00",
                "appEndDate": "2021-10-20T21:59:59+00:00",
                "appEndDate-ai": "2021-10-20T21:59:59+00:00",
                "appEndDate-ixd": "2021-10-20T21:59:59+00:00",
                "appEndDate-pm": "2021-10-20T21:59:59+00:00",
                "appEndDate-se": "2021-10-20T21:59:59+00:00",
                "appEndDate-pmc": "2021-10-20T21:59:59+00:00",
                "appEndDate-ac": "2021-10-20T21:59:59+00:00"
            }
        }}

    def test_after_init_database_not_empty(self):
        repository = FirestoreBatchRepository(self.db)
        assert(len(repository.list().list) > 0)

    def test_can_retrieve_single_batch_with_list(self):
        repository = FirestoreBatchRepository(self.db)
        res = repository.list([15]).list

        assert(len(res) == 1)
        assert(res[0].batch == 15)

    def test_can_retrieve_multiple_batches_with_list(self):
        repository = FirestoreBatchRepository(self.db)
        res = repository.list([15, 16]).list
        ids = sorted([b.batch for b in res])

        assert(ids == [15, 16])


