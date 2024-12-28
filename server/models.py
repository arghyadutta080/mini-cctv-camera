from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class FaceDetection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    face_count = db.Column(db.Integer, nullable=True)
