from Backend.DataTypes.Comment import Comment
from Backend.DataTypes.CommentList import CommentList
from Backend.GraphQL.shared import query, batches, incorrect_parameter
from graphql import GraphQLError


@query.field("applicantComments")
def resolve_applicant_details(_, info, batch_id, applicant_id):
    comments_array = []
    batch_doc = batches.document('batch-' + str(batch_id))
    incorrect_parameter(batch_doc)

    applications = batch_doc.collection('applications')
    application = applications.document(str(applicant_id))
    incorrect_parameter(application)

    commentsCollection = application.collection('comments')
    comments = [doc for doc in commentsCollection.stream()]
    for comment in comments:
        print(comment)
        commentid = comment.id
        comment = comment.to_dict()
        try:
            comments_array.append(Comment(
                commentid,
                comment['createdAt'],
                comment['updatedAt'] if 'updatedAt' in comment else None,
                comment['body'],
                comment['user']
            ))
        except KeyError as err:
            return GraphQLError(message="The field" + str(err) + "does not exists in the database document")
    return CommentList(comments_array)
