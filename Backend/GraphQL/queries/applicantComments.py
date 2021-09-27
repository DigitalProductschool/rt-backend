from Backend.Authentication.verify_token import get_user_context
from Backend.DataTypes.Exceptions.IncorrectParameterException import IncorrectParameterException
from Backend.DataTypes.Exceptions.AuthenticationException import AuthenticationException

from Backend.DataTypes.Comment import Comment
from Backend.DataTypes.CommentList import CommentList
from Backend.GraphQL.shared import query, batches

@query.field("applicantComments")
def resolve_applicant_details(_, info, batch_id, applicant_id):
    current_user = get_user_context(info)
    comments_array = []
    if (current_user):
        batch_doc = batches.document('batch-' + str(batch_id))
        if not batch_doc.get().exists:
            return IncorrectParameterException(errorMessage='Incorrect batch_id parameter')

        applications = batch_doc.collection('applications')
        application = applications.document(str(applicant_id))
        if not application.get().exists:
            return IncorrectParameterException(errorMessage='Incorrect applicant_id')
        
        commentsCollection = application.collection('comments')
        comments = [doc for doc in commentsCollection.stream()]
        for comment in comments:
            comment_dict = comment.to_dict()
            try:
                comments_array.append(Comment(
                                        comment.id,
                                        comment_dict['createdAt'],
                                        comment_dict['updatedAt'] if 'updatedAt' in comment_dict else None,
                                        comment_dict['body'],
                                        comment_dict['user']
                                        ))
            except KeyError as err:
                    return IncorrectParameterException(1, "The field" + str(err) + "does not exists in the database document" )
        return CommentList(comments_array)   
    else:
        return AuthenticationException()