from flask import Flask, redirect, url_for, session, Blueprint, jsonify
from authlib.integrations.flask_client import OAuth
import os
from Backend import oauth
from Backend.config import Config
from Backend.Authentication.auth_decorator import login_required
from flask import current_app as app


authentication = Blueprint('authentication', __name__)

authorized_emails = [
    "bela.sinoimeri@unternehmertum.de", "bedo@unternehmertum.de"]


google = oauth.register(
    name='google',
    client_id=Config.GOOGLE_CLIENT_ID,
    client_secret=Config.GOOGLE_CLIENT_SECRET,
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',
    client_kwargs={'scope': 'openid email profile'},
)


@authentication.route('/')
@login_required
def hello_world():
    email = dict(session)['profile']['email']
    return jsonify('You are logged in as {email}!')


@authentication.route('/login')
def login():
    google = oauth.create_client('google')
    redirect_uri = url_for('authentication.authorize', _external=True)
    return google.authorize_redirect(redirect_uri)


@authentication.route('/authorize')
def authorize():
    google = oauth.create_client('google')
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    user_info = resp.json()
    print(user_info["email"])
    if user_info["email"] not in authorized_emails: 
        return jsonify('The email address is not authorized!')
    user = oauth.google.userinfo()
    session['profile'] = user_info
    session.permanent = True
    return redirect('/')


@authentication.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/')
