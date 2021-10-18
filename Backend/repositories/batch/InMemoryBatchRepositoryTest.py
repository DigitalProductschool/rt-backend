import unittest

from Backend.repositories.batch.InMemoryBatchRepository import InMemoryBatchRepository


class InMemoryBatchRepositoryTest(unittest.TestCase):

    def test_after_init_database_not_empty(self):
        repository = InMemoryBatchRepository()
        assert (len(repository.list().list) > 0)

    def test_can_retrieve_existing_batch(self):
        repository = InMemoryBatchRepository()
        assert (repository.get(15).batch == 15)

    def test_not_existing_repository_throws_keyerror(self):
        repository = InMemoryBatchRepository()
        with self.assertRaises(KeyError) as cm:
            repository.get(10)

