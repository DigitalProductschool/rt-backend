from ariadne import UnionType
from Backend.DataTypes.Applicant import Applicant
from Backend.DataTypes.ApplicantList import ApplicantList
from Backend.DataTypes.TeamList import TeamList
from Backend.DataTypes.User import User
from Backend.DataTypes.UserList import UserList
from Backend.DataTypes.BatchList import BatchList
from Backend.DataTypes.CommentList import CommentList
from Backend.DataTypes.CompanyList import CompanyList
from Backend.DataTypes.MentionList import MentionList
from Backend.DataTypes.Program import Program

from Backend.DataTypes.ProgramList import ProgramList
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

TeamsQueryResult = UnionType("TeamsQueryResult")
@TeamsQueryResult.type_resolver
def resolve_teams_query_result(obj, *_):
    if isinstance(obj, TeamList):
        return "TeamList"
    if isinstance(obj, GraphQLError):
        return "Exception"
    return None

CompaniesQueryResult = UnionType("CompaniesQueryResult")
@CompaniesQueryResult.type_resolver
def resolve_companies_query_result(obj, *_):
    if isinstance(obj, CompanyList):
        return "CompanyList"
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

UserMentionsQueryResult = UnionType("UserMentionsQueryResult")
@UserMentionsQueryResult.type_resolver
def resolve_user_mentions_query_result(obj, *_):
    if isinstance(obj, MentionList):
        return "MentionList"
    if isinstance(obj, GraphQLError):
        return "Exception"
    return None

ProgramsQueryResult = UnionType("ProgramsQueryResult")
@ProgramsQueryResult.type_resolver
def resolve_programs_query_result(obj, *_):
    if isinstance(obj, ProgramList):
        return "ProgramList"
    if isinstance(obj, GraphQLError):
        return "Exception"
    return None

ProgramDetailsQueryResult = UnionType("ProgramDetailsQueryResult")
@ProgramDetailsQueryResult.type_resolver
def resolve_program_details_query_result(obj, *_):
    if isinstance(obj, Program):
        return "Program"
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
