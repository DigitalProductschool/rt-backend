# appEndDate - application End Date
from Backend.DataTypes.Exceptions.IncorrectParameterException import IncorrectParameterException


class Batch:
    def __init__(self, batch, startDate, endDate, appStartDate, appEndDate, appEndDateAI, appEndDateIXD, appEndDatePM,
                 appEndDateSE):
        self.batch = batch
        self.startDate = startDate
        self.endDate = endDate
        self.appStartDate = appStartDate
        self.appEndDate = appEndDate
        self.appEndDateAI = appEndDateAI
        self.appEndDateIXD = appEndDateIXD
        self.appEndDatePM = appEndDatePM
        self.appEndDateSE = appEndDateSE


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
                      b['appEndDate-se']
                      )
            return batch
        except KeyError as err:
            IncorrectParameterException(1, "The field" + str(err) + "does not exists in the database document")
