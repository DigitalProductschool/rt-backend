from flask import request
from flask import Blueprint
from Backend.UserManagement.authentication import verify_token
from Backend.UserManagement.authorization import verify_authorization
from Backend.GraphQL.shared import users

usermanagement = Blueprint('usermanagement', __name__)


def save_user_document(user):
    user_doc = users.document(user.uid)
    if not user_doc.get().exists:
        data = {
            u'name': user.name,
            u'email': user.email,
            u'photo': user.photo,
            u'role': user.role,
        }
        user_doc.set(data)
    return user_doc

def get_user_context():
    context = {}
    context['request'] = request
    context['user'] = None
    if "Authorization" in request.headers:
        auth = request.headers["Authorization"]
        scheme, token = auth.split()
        if scheme.lower() != 'bearer':
            return context
        uid = verify_token(token)
        if not uid:
            return context
        current_user = verify_authorization(uid)
        save_user_document(current_user)
        context['user'] = current_user
        return context
