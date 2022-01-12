from Backend.DataTypes.Company import Company
from Backend.DataTypes.CompanyList import CompanyList
from Backend.GraphQL.shared import query, companies, incorrect_parameter

@query.field("companies")
def resolve_companies(_, info):
    companiesArray=[]
    for company in companies.stream():
        company_doc = companies.document(company.id) 
        incorrect_parameter(company_doc)
        company_details = company_doc.get().to_dict()
        companiesArray.append(Company(
            company_details["id"], company_details["name"], company_details["logo"]))
    return CompanyList(companiesArray)
