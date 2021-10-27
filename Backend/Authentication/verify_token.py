from flask import request, jsonify
from functools import wraps
from firebase_admin import auth
from flask import Blueprint
from Backend.database import db
from Backend.DataTypes.User import User

authentication = Blueprint('authentication', __name__)

def verify_token(id_token):
    try:
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        return uid
    except:
        return None

def verify_email(email):
    white_list = ["marcus.paeschke@unternehmertum.de", "bela.sinoimeri@unternehmertum.de", "bela.sinoimeri@dpschool.io", "rieder@unternehmertum.de", "magda.nowak-trzos@unternehmertum.de","bedo@unternehmertum.de", "asaei@unternehmertum.de", "tobias.kalkowsky@unternehmertum.de"]
    if email not in white_list: 
        return None
    else: 
        return True

def get_user_data(uid):
    try:
        user = auth.get_user(uid)
        if verify_email(user.email): 
            current_user = User(
                      user.uid,
                      user.display_name,
                      user.email,
                      user.photo_url
                      )
            return current_user
    except:
        return None

def save_users(current_user): 
    try: 
       doc_ref = db.collection('users').document(current_user.uid)
       doc = doc_ref.get()
       if doc.exists: 
          return None
       else: 
           data = {
           u'name': current_user.name,
           u'email': current_user.email,
           u'photo': current_user.photo,
           u'role': current_user.role,
           }
           doc_ref.set(data)
           return doc
    except:
        return None

def get_user_context(info):
    try: 
      request = info.context
      auth = request.headers["Authorization"]
      scheme, token = auth.split()
      uid = verify_token(token)
      if(uid): 
            current_user = get_user_data(uid)
            saved = save_users(current_user)
            return current_user
    except: 
        return None



