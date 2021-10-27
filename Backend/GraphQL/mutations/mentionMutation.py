from Backend.GraphQL.shared import mutation, get_user_document, get_current_user, get_comment_document, incorrect_parameter
from Backend.DataTypes.Status import Status
from firebase_admin import firestore
from graphql import GraphQLError

@mutation.field("createMention")
def resolve_create_mention(_, info, batch_id, applicant_id, comment_id, mentioned_id):
    current_user = get_current_user(info)
    try:
            user_doc, _ = get_user_document(mentioned_id)
    except Exception as err:
            return GraphQLError(message=err.__str__())

    mention_doc = user_doc.collection('mentions').document()
    mentioner_user = {
            'uid': current_user.uid,
            'name': current_user.name,
            'photo': current_user.photo
        }
    get_comment_document(batch_id, applicant_id)
    mention_data = {
            'applicantId': applicant_id,
            'commentId': comment_id,
            'batchId': batch_id,
        }

    mention_date = firestore.SERVER_TIMESTAMP
    mention_doc.set({'mentionData': mention_data, 'mentioner': mentioner_user,
                         'createdAt': mention_date, 'new': bool(True)})
    return Status(0, "Mention added succesfully")

@mutation.field("readMention")
def resolve_create_mention(_, info, mention_id):
    current_user = get_current_user(info)
    try:
            user_doc, _ = get_user_document(current_user.uid)
    except Exception as err:
            return GraphQLError(message=err.__str__())

    mention = user_doc.collection('mentions').document(mention_id)
    incorrect_parameter(mention)
    mention.update({'new': bool(False)})
    return Status(0, "Mention updated succesfully")