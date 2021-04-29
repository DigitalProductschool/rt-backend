from flask import Flask
from Backend.config import Config
from authlib.integrations.flask_client import OAuth
from flask_cors import CORS

oauth = OAuth()
cors = CORS()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    oauth.init_app(app)
    cors.init_app(app)
    
    from Backend.Authentication.routes import authentication
    from Backend.GraphQL.routes import graphql

    app.register_blueprint(authentication)
    app.register_blueprint(graphql)

    return app
