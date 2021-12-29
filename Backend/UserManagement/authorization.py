from firebase_admin import auth
from Backend.DataTypes.User import User

# Better saved in the db -> When we do the migration of db


def verify_email(email):
    white_list = ["stockerl@unternehmertum.de","marcus.paeschke@unternehmertum.de",
                  "philip.prestele@unternehmertum.de", 
                  "samreen.azam@unternehmertum.de",
                  "bela.sinoimeri@unternehmertum.de",
                  "magda.nowak-trzos@unternehmertum.de",
                  "bedo@unternehmertum.de",
                  "asaei@unternehmertum.de",
                  "tobias.kalkowsky@unternehmertum.de",
                  "kastner@unternehmertum.de",
                  "rieder@unternehmertum.de",
                  "natthagorn.bunnet@unternehmertum.de"]
    if email not in white_list:
        return None
    else:
        return True


def verify_authorization(uid):
    user = auth.get_user(uid)
    if verify_email(user.email):
        current_user = User(
            user.uid,
            user.display_name,
            user.email,
            user.photo_url
        )
        return current_user
    else:
        return None
