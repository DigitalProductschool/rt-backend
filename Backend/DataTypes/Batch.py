from graphql import GraphQLError


class Batch():
    def __init__(self, batch, startDate, endDate, appStartDate, appEndDate, appEndDateAI=None, appEndDateIXD=None,
                 appEndDatePM=None, appEndDateSE=None, appEndDatePMC=None, appEndDateAC=None):

        self.batch = batch
        self.startDate = startDate
        self.endDate = endDate
        self.appStartDate = appStartDate
        self.appEndDate = appEndDate
        self.appEndDateAI = appEndDateAI
        self.appEndDateIXD = appEndDateIXD
        self.appEndDatePM = appEndDatePM
        self.appEndDateSE = appEndDateSE
        self.appEndDatePMC = appEndDatePMC
        self.appEndDateAC = appEndDateAC

    @classmethod
    def from_dict(cls, b):
        try:
            batch = Batch(b['batch'],
                          b['startDate'],
                          b['endDate'],
                          b['appStartDate'],
                          b['appEndDate'],
                          b['appEndDate-ai'],
                          b['appEndDate-ixd'],
                          b['appEndDate-pm'],
                          b['appEndDate-se'],
                          b['appEndDate-pmc'],
                          b['appEndDate-ac'],
                          )
            return batch
        except KeyError as err:
            raise GraphQLError(message="The field" + str(err) + "does not exists in the database document")
