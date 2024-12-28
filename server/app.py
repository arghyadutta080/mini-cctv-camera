from flask import Flask, Response, jsonify, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
from video_stream import generate_frames
from models import db, FaceDetection

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)
migrate = Migrate(app, db)
CORS(app)


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/metadata', methods=['GET'])
def get_metadata():
    detections = FaceDetection.query.all()
    return jsonify([{'id': d.id, 'timestamp': d.timestamp, 'face_count': d.face_count} for d in detections])


@app.route('/log_detection', methods=['POST'])
def log_detection():
    # Simulated face detection logging
    data = request.get_json()
    detection = FaceDetection(timestamp=datetime.fromisoformat(
        data['timestamp']), face_count=int(data['face_count']))
    db.session.add(detection)
    db.session.commit()
    return jsonify({'message': 'Detection logged!'}), 201


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
