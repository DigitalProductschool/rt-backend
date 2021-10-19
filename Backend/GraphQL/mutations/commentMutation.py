from Backend.GraphQL.shared import mutation, get_current_user, get_comment_document
from Backend.DataTypes.Status import Status
from firebase_admin import firestore


@mutation.field("createComment")
def resolve_create_comment(_, info, batch_id, applicant_id, comment_body):
    comment_doc = get_comment_document(batch_id, applicant_id)
    current_user = get_current_user(info)
    comment_user = {
        'uid': current_user.uid,
        'name': current_user.name,
        'photo': current_user.photo
    }
    comment_date = firestore.SERVER_TIMESTAMP
    comment_doc.set(
        {'body': comment_body, 'user': comment_user, 'createdAt': comment_date})
    return Status(0, "Comment added succesfully")


@mutation.field("editComment")
def resolve_edit_comment(_, info, batch_id, applicant_id, comment_body, comment_id):
    comment_doc = get_comment_document(
        info, batch_id, applicant_id, comment_id)
    comment_date = firestore.SERVER_TIMESTAMP
    comment_doc.update({'body': comment_body, 'updatedAt': comment_date})
    return Status(0, "Comment updated succesfully")


@mutation.field("deleteComment")
def resolve_delete_comment(_, info, batch_id, applicant_id, comment_id):
    get_comment_document(info, batch_id, applicant_id, comment_id).delete()
    return Status(0, "Comment deleted succesfully")
