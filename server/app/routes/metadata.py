from flask import Blueprint, jsonify, request
from app.models import FaceDetection
from app import db
from datetime import datetime

metadata_bp = Blueprint('metadata', __name__)

@metadata_bp.route('/', methods=['GET'])
def get_metadata():
    detections = FaceDetection.query.all()
    return jsonify([{'id': d.id, 'timestamp': d.timestamp, 'face_count': d.face_count} for d in detections])

@metadata_bp.route('/log', methods=['POST'])
def log_detection():
    # Simulated face detection logging
    data = request.get_json()
    detection = FaceDetection(timestamp=datetime.fromisoformat(
        data['timestamp']), face_count=int(data['face_count']))
    db.session.add(detection)
    db.session.commit()
    return jsonify({'message': 'Detection logged!'}), 201
