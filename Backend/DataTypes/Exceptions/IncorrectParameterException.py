class IncorrectParameterException():
     def __init__(self, code=400, errorMessage='Object not found - check if given prameters are valid'):
         self.code = code
         self.message = errorMessage
