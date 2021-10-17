from flask import Flask
from Backend.config import config
from flask_cors import CORS
cors = CORS()

def create_app(config_class=config):
    app = Flask(__name__)
    app.config.from_object(config)
    cors.init_app(app)
    from Backend.GraphQL.routes import graphql
    from Backend.UserManagement.context import usermanagement

    app.register_blueprint(graphql)
    app.register_blueprint(usermanagement)
    
    return app
