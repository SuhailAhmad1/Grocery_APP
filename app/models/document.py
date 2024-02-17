from app import db
from datetime import datetime

class Document(db.Model):
    __tablename__ = "user_docs"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    doc_path = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    edited_at = db.Column(db.DateTime, default=datetime.now())
    processing_time = db.Column(db.Integer, default=0)
    output = db.Column(db.String)
    is_edited = db.Column(db.Boolean, default=False)