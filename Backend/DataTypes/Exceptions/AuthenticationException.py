class AuthenticationException():
     def __init__(self, code=404, errorMessage='User does not have permissions'):
         self.code = code
         self.message = errorMessage
