from flask import Flask
from Backend.config import Config
from flask_cors import CORS

cors = CORS()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    cors.init_app(app)
    
    from Backend.GraphQL.routes import graphql
    from Backend.Authentication.verify_token import authentication

    app.register_blueprint(graphql)
    app.register_blueprint(authentication)
    
    return app
