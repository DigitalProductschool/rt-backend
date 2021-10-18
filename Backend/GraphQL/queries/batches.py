
from Backend.Authentication.verify_token import get_user_context
from Backend.DataTypes.Exceptions.AuthenticationException import AuthenticationException


from Backend.GraphQL.shared import query
from Backend.repositories.batch.FirestoreBatchRepository import FirestoreBatchRepository


@query.field("batches")
def resolve_batches(_, info, batch_id_list):
    current_user = get_user_context(info)

    if current_user:
        repository = FirestoreBatchRepository()
        return repository.list(batch_id_list)
    else:
        return AuthenticationException()



