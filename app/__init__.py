from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from app.config import DevelopmentConfig

db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    cors = CORS(app, resources={r"*": {"origins": "*"}})

    JWTManager(app)
    db.init_app(app)
    migrate = Migrate(app, db) 
    # Additional app setup code here
    return app

