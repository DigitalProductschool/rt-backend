
from Backend.Authentication.verify_token import get_user_context
from Backend.DataTypes.Exceptions.IncorrectParameterException import IncorrectParameterException
from Backend.DataTypes.Exceptions.AuthenticationException import AuthenticationException

from Backend.DataTypes.Batch import Batch
from Backend.DataTypes.BatchList import BatchList
from Backend.GraphQL.shared import query, batch_details

@query.field("batches")
def resolve_batches(_, info, batch_id_list):
    current_user = get_user_context(info)
    batches = []
    if (current_user):
        if len(batch_id_list) > 0: 
            batches_collection = [doc.to_dict() for doc in batch_details.stream() if doc.to_dict()['batch'] in batch_id_list]
        else: 
            batches_collection = [doc.to_dict() for doc in batch_details.stream()]
        for batch in batches_collection:
            try:
                batches.append(Batch(batch['batch'],
                                    batch['startDate'],
                                    batch['endDate'],
                                    batch['appStartDate'],
                                    batch['appEndDate'],
                                    batch['appEndDate-ai'],
                                    batch['appEndDate-ixd'],
                                    batch['appEndDate-pm'],
                                    batch['appEndDate-se']
                                    ))
            except KeyError as err:
                    return IncorrectParameterException(1, "The field" + str(err) + "does not exists in the database document" )
        return BatchList(batches)
    else:
        return AuthenticationException()

