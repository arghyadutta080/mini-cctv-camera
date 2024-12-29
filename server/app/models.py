from app import db
from datetime import datetime


class FaceDetection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    face_count = db.Column(db.Integer, nullable=True)
