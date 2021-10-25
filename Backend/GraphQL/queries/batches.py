from Backend.DataTypes.Batch import Batch
from Backend.DataTypes.BatchList import BatchList
from Backend.GraphQL.shared import query, batch_details, incorrect_parameter
from graphql import GraphQLError
from Backend.GraphQL.shared import query
from Backend.repositories.batch.FirestoreBatchRepository import FirestoreBatchRepository
from Backend.database import db


@query.field("batches")
def resolve_batches(_, info, batch_id_list):

    repository = FirestoreBatchRepository(db)
    res = repository.list(batch_id_list)
    if not res:
        raise GraphQLError(message="Incorrect parameter")

    return res
