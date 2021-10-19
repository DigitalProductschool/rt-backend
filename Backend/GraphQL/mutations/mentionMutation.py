from Backend.UserManagement.context import get_user_context
from Backend.DataTypes.Exceptions.AuthenticationException import AuthenticationException
from Backend.DataTypes.Exceptions.IncorrectParameterException import IncorrectParameterException

from Backend.GraphQL.shared import mutation, get_user_document
from Backend.DataTypes.Status import Status
from firebase_admin import firestore
from graphql import GraphQLError

@mutation.field("createMention")
def resolve_create_mention(_, info, batch_id, applicant_id, comment_id, mentioned_id):
    current_user = get_user_context()
    if(current_user):
        try:
            user_doc, _ = get_user_document(mentioned_id)
        except Exception as err:
            return GraphQLError(message=err.__str__())

        mention_doc = user_doc.collection('mentions').document()
        mentioner_user = {
            'uid': current_user.uid,
            'name': current_user.name,
            'photo': current_user.photo,
            'email': current_user.email,
        }
        mention_data = {
            'applicantId': applicant_id,
            'commentId': comment_id,
            'batchId': batch_id,
        }

        mention_date = firestore.SERVER_TIMESTAMP
        mention_doc.set({'mentionData': mention_data, 'mentioner': mentioner_user,
                         'createdAt': mention_date, 'read': bool('false')})
        return Status(0, "Mention added succesfully")
    else:
        return AuthenticationException()
