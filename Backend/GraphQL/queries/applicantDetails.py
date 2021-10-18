from Backend.GraphQL.shared import query, batches, incorrect_parameter, create_applicant


@query.field("applicantDetails")
def resolve_applicant_details(_, info, batch_id, applicant_id):
    batch_doc = batches.document('batch-' + str(batch_id))
    incorrect_parameter(batch_doc)

    applications = batch_doc.collection('applications')
    application = applications.document(str(applicant_id))
    incorrect_parameter(application)

    applicant = application.get().to_dict()
    return create_applicant(applicant)
