from flask import Blueprint
from app.controllers.user_controller import upload_doc
user_routes = Blueprint('user', __name__, url_prefix="/api/user")

user_routes.route("/upload_doc", methods=["POST"])(upload_doc)