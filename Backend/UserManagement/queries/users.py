from Backend.UserManagement.context import get_user_context
from Backend.DataTypes.User import User
from Backend.DataTypes.UserList import UserList
from Backend.GraphQL.shared import query, users, get_user_document
from Backend.GraphQL.shared import protected_endpoint

@query.field("users")
@protected_endpoint
def resolve_users(_, info):
     usersArray=[]
     for user in users.stream():
          user_doc, user_details = get_user_document(info, user.id)
          usersArray.append(User(user.id, user_details["name"], user_details["email"], user_details["photo"]))
          print(f'{user.id} => {user.to_dict()}')
     return UserList(usersArray)