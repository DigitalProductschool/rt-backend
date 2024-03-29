from graphql import GraphQLError


class Team():
    def __init__(self, uid, name, batch, members, companies ):
        self.id = uid
        self.name = name
        self.batch = batch
        self.members = members
        self.companies = companies


    @classmethod
    def from_dict(cls, t):
        try:
            team = Team(t['id'],
                        t['name'],
                        t['batch'],
                        t['members'],
                        t['companies'],
                        )
            return team
        except KeyError as err:
            raise GraphQLError(message="The field" + str(err) + "does not exists in the database document")

        