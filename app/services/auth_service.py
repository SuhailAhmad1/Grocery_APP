from app.models.user import User
from app import db
import traceback
from passlib.hash import pbkdf2_sha256 as sha256

class AuthService:
    def get_user_by_email(self, email):
        try:
            user = User.query.filter_by(email = email).first()
            if user:
                return {
                    "email": user.email,
                    "username": user.username,
                    "password": user.password, 
                    "id": user.id
                    }
            else:
                return {}
        except Exception as e:
            print(traceback.print_exc(e))
            return False
        
    def create_new_user(self, data):
        try:
            data["password"] = sha256.hash(data["password"])
            new_user = User(data["username"], data["email"], data["password"])
            db.session.add(new_user)
            db.session.commit()
            return True
        except Exception as e:
            print(traceback.print_exc(e))
            return False
        
    def get_all_users(self):
        users = User.query.all()
        return [user.username for user in users]
