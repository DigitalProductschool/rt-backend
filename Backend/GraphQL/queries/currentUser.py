
from Backend.Authentication.verify_token import get_user_context
from Backend.GraphQL.shared import query

@query.field("user")
def resolve_current_user(_, info):
     authentication = get_user_context(info)
     return authentication
   