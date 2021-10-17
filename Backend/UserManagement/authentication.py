from firebase_admin import auth
from Backend.DataTypes.Exceptions.AuthenticationException import AuthenticationException

def verify_token(id_token):
    try:
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        return uid
    except:
        return AuthenticationException()