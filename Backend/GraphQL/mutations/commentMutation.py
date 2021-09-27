from Backend.Authentication.verify_token import get_user_context
from Backend.DataTypes.Exceptions.AuthenticationException import AuthenticationException
from Backend.DataTypes.Exceptions.IncorrectParameterException import IncorrectParameterException

from Backend.GraphQL.shared import mutation, get_applicant_document
from Backend.DataTypes.Status import Status
from firebase_admin import firestore

@mutation.field("createComment")
def resolve_create_comment(_, info, batch_id, applicant_id, comment_body):
    current_user = get_user_context(info)
    if(current_user):
        try:
            application_doc, application_details = get_applicant_document(info, batch_id, applicant_id)
        except Exception as err:
            return IncorrectParameterException(errorMessage=err.__str__())

        comment_doc = application_doc.collection('comments').document()
        comment_user = {
            'uid': current_user.uid,
            'name': current_user.name,
            'photo': current_user.photo, 
            'email': current_user.email, 
        }
        comment_date = firestore.SERVER_TIMESTAMP
        comment_doc.set({'body': comment_body, 'user': comment_user, 'createdAt': comment_date})
        return Status(0, "Comment added succesfully")
    else:
        return AuthenticationException()



@mutation.field("editComment")
def resolve_edit_comment(_, info, batch_id, applicant_id, comment_body, comment_id):
    current_user = get_user_context(info)
    if(current_user):
        try:
            application_doc, application_details = get_applicant_document(info, batch_id, applicant_id)
        except Exception as err:
            return IncorrectParameterException(errorMessage=err.__str__())

        comment_doc = application_doc.collection('comments').document(comment_id)
        comment_date = firestore.SERVER_TIMESTAMP
        comment_doc.update({'body': comment_body, 'updatedAt': comment_date})
        return Status(0, "Comment updated succesfully")
    else:
        return AuthenticationException()


@mutation.field("deleteComment")
def resolve_delete_comment(_, info, batch_id, applicant_id, comment_id):
    current_user = get_user_context(info)
    if(current_user):
        try:
            application_doc, application_details = get_applicant_document(info, batch_id, applicant_id)
        except Exception as err:
            return IncorrectParameterException(errorMessage=err.__str__())

        application_doc.collection('comments').document(comment_id).delete()
        return Status(0, "Comment deleted succesfully")
    else:
        return AuthenticationException()