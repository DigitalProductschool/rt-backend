from ariadne import QueryType
from DataTypes.Applicant import Applicant

query = QueryType()
Applicants = []


@query.field("applicants")
def resolve_orders(_, info):
    # request to the database
    return Applicants