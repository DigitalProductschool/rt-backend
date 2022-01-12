from graphql import GraphQLError


class Team():
    def __init__(self, uid, name, batch_id, members, companies ):
        self.id = uid
        self.name = name
        self.batch_id = batch_id
        self.members = members
        self.companies = companies


    @classmethod
    def from_dict(cls, t):
        try:
            team = Team(t['id'],
                        t['name'],
                        t['batch_id'],
                        t['members'],
                        t['companies'],
                        )
            return team
        except KeyError as err:
            raise GraphQLError(message="The field" + str(err) + "does not exists in the database document")

        