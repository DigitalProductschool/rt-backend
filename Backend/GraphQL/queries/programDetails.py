from Backend.DataTypes.Program import Program
from Backend.DataTypes.ProgramList import ProgramList
from Backend.GraphQL.shared import query, programs, get_program_document

@query.field("programDetails")
def resolve_program_details(_, info, program_id):
     program_details = get_program_document(program_id)
     return Program(program_details["id"], program_details["short"], program_details["title"])