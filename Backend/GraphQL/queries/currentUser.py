from Backend.GraphQL.shared import query, get_current_user


@query.field("user")
def resolve_current_user(_, info):
    user = get_current_user(info)
    return user
