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

def get_user_data(uid):
    try:
        user = auth.get_user(uid)
        current_user = User(user.uid,
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
           u'uid': current_user.uid,
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
            return True
    except: 
        return None


