class AuthenticationException():
     def __init__(self, code, errorMessage):
         self.code = code
         self.message = errorMessage
