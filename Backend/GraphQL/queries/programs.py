from Backend.DataTypes.Program import Program
from Backend.DataTypes.ProgramList import ProgramList
from Backend.GraphQL.shared import query, programs, get_program_document

@query.field("programs")
def resolve_programs(_, info):
    programsArray = []
    for program in programs.stream():
        program_details = get_program_document(program.id)
        programsArray.append(Program(
            program.id, program_details["short"], program_details["title"]))
    return ProgramList(programsArray)
