from Backend.GraphQL.shared import users

def get_user_document(user_id): 
    user_doc = users.document(user_id)
    if not user_doc.get().exists:
        raise Exception("Invalid user id") 
    user_details = user_doc.get().to_dict()
    return user_doc, user_details

def save_user_document(user): 
    user_doc = users.document(user.uid)
    if not user_doc.get().exists:
        data = {
           u'name': user.name,
           u'email': user.email,
           u'photo': user.photo,
           u'role': user.role,
           }
           user_doc.set(data)
    return user_doc
