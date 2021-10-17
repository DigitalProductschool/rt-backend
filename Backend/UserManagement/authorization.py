from firebase_admin import auth
from Backend.DataTypes.Exceptions.AuthenticationException import AuthenticationException

# Better saved in the db -> When we do the migration of db
def verify_email(email):
    white_list = ["marcus.paeschke@unternehmertum.de", 
    "bela.sinoimeri@unternehmertum.de",
    "magda.nowak-trzos@unternehmertum.de",
    "bedo@unternehmertum.de", 
    "asaei@unternehmertum.de", 
    "tobias.kalkowsky@unternehmertum.de", 
    "rieder@unternehmertum.de"]
    if email not in white_list: 
        return AuthenticationException()
    else: 
        return True

def verify_authorization(uid): 
    current_user = auth.get_user(uid)
    if verify_email(user.email): 
        current_user = User(
                      user.uid,
                      user.display_name,
                      user.email,
                      user.photo_url
                      )
        return current_user
    else: 
        return AuthenticationException()
