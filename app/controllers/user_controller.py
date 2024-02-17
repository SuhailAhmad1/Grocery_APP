import traceback
from passlib.hash import pbkdf2_sha256 as sha256
from flask import request
from app.services.user_service import UserService
from app.utils import build_cors_preflight_response
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity

user_service = UserService()
ALLOWED_EXTENSIONS = {'pdf'}

def upload_doc():
    try:
        if request.method == "OPTIONS":
            return build_cors_preflight_response()
        userid = get_jwt_identity()
        if 'docs' not in request.files:
            print("No file part")
            return {"message":"Document is missing or blank"}, 400
        if len(request.files.getlist('doc')) > 1:
            print(f"More than {1} files uploaded")
            return {"message": "You can only upload 1 doc at a time"}, 400
        for doc in request.files.getlist('doc'):
            if not allowed_file(doc.filename):
                print("Extension Issue")
                return {"message": "Invalid file type"}, 400
            if doc.filename == '':
                print('No selected file')
                return {"message": "No files were found in the request"}, 400
        status, message = user_service.upload_doc(userid, request.files)
        if status:
            return {"message": "Document Uploaded Successfully, Running Analysis"}, 200
        else:
            return {"message":message}, 400
        
    except Exception as e:
        print(traceback.print_exc(e))
        return {"message": "Something went wrong"}, 500

def allowed_file(doc_name):
    return '.' in doc_name and \
           doc_name.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
