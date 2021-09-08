class Form():
   def __init__(self, map):
     if map:
       self.location = map["location"]
       self.streetNumber = map["streetNumber"]
       self.addressSuffix = map["addressSuffix"]
       self.postcode = map["postcode"]
       self.city = map["city"]
       self.country = map["country"]
       self.accountHolder = map["accountHolder"]
       self.bankName = map["bankName"]
       self.iban = map["iban"]
       self.bic = map["bic"]
       self.shirtSize = map["shirtSize"]
       self.shirtStyle = map["shirtStyle"]
       self.foodIntolerances  = map["foodIntolerances"]