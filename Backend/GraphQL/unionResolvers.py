from ariadne import UnionType
from Backend.DataTypes.Applicant import Applicant
from Backend.DataTypes.ApplicantList import ApplicantList
from Backend.DataTypes.User import User
from Backend.DataTypes.UserList import UserList
from Backend.DataTypes.BatchList import BatchList
from Backend.DataTypes.CommentList import CommentList
from Backend.DataTypes.Status import Status
from graphql import GraphQLError

# Queries resolvers
ApplicantsQueryResult = UnionType("ApplicantsQueryResult")
@ApplicantsQueryResult.type_resolver
def resolve_applicants_query_result(obj, *_):
    if isinstance(obj, ApplicantList):
        return "ApplicantList"
    if isinstance(obj, GraphQLError):
        return "Exception"
    return None

CommentsQueryResult = UnionType("CommentsQueryResult")
@CommentsQueryResult.type_resolver
def resolve_comments_query_result(obj, *_):
    if isinstance(obj, CommentList):
        return "CommentList"
    if isinstance(obj, GraphQLError):
        return "Exception"
    return None

ApplicantDetailsQueryResult = UnionType("ApplicantDetailsQueryResult")
@ApplicantDetailsQueryResult.type_resolver
def resolve_applicant_details_query_result(obj, *_):
    if isinstance(obj, Applicant):
        return "Applicant"
    if isinstance(obj, GraphQLError):
        return "Exception"
    return None


BatchesQueryResult = UnionType("BatchesQueryResult")
@BatchesQueryResult.type_resolver
def resolve_batches_query_result(obj, *_):
    if isinstance(obj, BatchList):
        return "BatchList"
    if isinstance(obj, GraphQLError):
        return "Exception"
    return None


UserQueryResult = UnionType("UserQueryResult")
@UserQueryResult.type_resolver
def resolve_user_query_result(obj, *_):
    if isinstance(obj, User):
        return "User"
    if isinstance(obj, GraphQLError):
        return "Exception"
    return None

UsersQueryResult = UnionType("UsersQueryResult")
@UsersQueryResult.type_resolver
def resolve_users_query_result(obj, *_):
    if isinstance(obj, UserList):
        return "UserList"
    if isinstance(obj, GraphQLError):
        return "Exception"
    return None


# Mutation resolvers
MutationResult = UnionType("MutationResult")
@MutationResult.type_resolver
def resolve_mutation_result(obj, *_):
    if isinstance(obj, Status):
        return "Status"
    if isinstance(obj, GraphQLError):
        return "Exception"
    return None
