from flask import request
from flask import Blueprint
from Backend.UserManagement.authentication import verify_token
from Backend.UserManagement.authorization import verify_authorization
from Backend.UserManagement.users import save_user_document
from Backend.DataTypes.Exceptions.AuthenticationException import AuthenticationException

UserManagement = Blueprint('usermanagement', __name__)

def get_user_context(info):
    try: 
      request = info.context
      header = request.headers["Authorization"]
      scheme, token = header.split()
      uid = verify_token(token)
      if(uid): 
            current_user = verify_authorization(uid)
            save_user_document(current_user)
            return current_user
    except: 
        return AuthenticationException()



