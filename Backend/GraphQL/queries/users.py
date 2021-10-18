from Backend.DataTypes.User import User
from Backend.DataTypes.UserList import UserList
from Backend.GraphQL.shared import query, users, get_user_document


@query.field("users")
def resolve_users(_, info):
    usersArray = []
    for user in users.stream():
        print(user)
        _, user_details = get_user_document(info, user.id)
        usersArray.append(User(
            user.id, user_details["name"], user_details["email"], user_details["photo"]))
    return UserList(usersArray)
