class Scholarship():
    def __init__(self, name, monthlyAmount, totalAmount, bankAmount, offerDescription):
        self.name = name
        self.monthlyAmount = monthlyAmount
        self.totalAmount = totalAmount
        self.bankAmount = bankAmount
        self.offerDescription = offerDescription

Munich = Scholarship("Munich Onsite", "1000.00 euros", "3,000.00 euros", "985.00 euros", "You will also receive a monthly scholarship of 1000€.")
OECD = Scholarship("OECD country", "750.00 euros", "2,250.00 euros", "735.00 euros", "You will also receive a monthly scholarship of 750€.")
NonOECD = Scholarship("non OECD country", "450.00 euros and 50.00 euros as an internet grant in addition", "1,500.00 euros", "485.00 euros", "You will also receive a monthly scholarship of 500.00€  (incl. 50.00€ internet grant).")