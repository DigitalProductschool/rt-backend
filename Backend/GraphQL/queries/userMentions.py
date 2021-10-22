from Backend.GraphQL.shared import query, get_current_user, get_user_document
from Backend.DataTypes.Mention import Mention
from Backend.DataTypes.MentionList import MentionList
from graphql import GraphQLError

@query.field("userMentions")
def resolve_user_mentions(_, info):
    mentionarray = []
    current_user = get_current_user(info)
    try:
            user_doc, _ = get_user_document(current_user.uid)
    except Exception as err:
            return GraphQLError(message=err.__str__())

    mentions = user_doc.collection('mentions')
    mentions = [doc for doc in mentions.stream()]
    for mention in mentions:
            mention_dict = mention.to_dict()
            mentionarray.append(Mention(mention.id, mention_dict["createdAt"], mention_dict["mentionData"], mention_dict["mentioner"], mention_dict["new"]))
    return MentionList(mentionarray)