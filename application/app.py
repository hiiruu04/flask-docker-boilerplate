import os
from flask import Flask, jsonify
from flask.templating import render_template
from flask_cors import CORS

from application.models import db, migrate
from application.schema import schema
from application.auth import jwt
from application import routes

def create_app(config_name):

    app = Flask(__name__, instance_relative_config=True)
    config_module = f"flaskr.config.{config_name.capitalize()}Config"
    app.config.from_object(config_module)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config["SQLALCHEMY_ECHO"] = True
    # env_config = os.getenv("APP_SETTINGS", "flaskr.config.DevelopmentConfig")
    # app.config.from_object("flaskr.config.DevelopmentConfig")
    db.init_app(app)
    migrate.init_app(app, db)
    # schema.init_app(app)
    jwt.init_app(app)

    #* blueprint routes
    #* from .api import bp as api_bp
    #* app.register_blueprint(api_bp, url_prefix="/api")

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app