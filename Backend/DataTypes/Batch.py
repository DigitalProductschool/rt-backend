class Batch():
    def __init__(self, batch, startDate, endDate, appStartDate, appEndDate, appEndDateAI=None, appEndDateIXD=None, appEndDatePM=None,  appEndDateSE=None, appEndDatePMC=None, appEndDateAC=None):
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
