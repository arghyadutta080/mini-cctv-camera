from flask import Blueprint, Response
from app.utils.video_stream import generate_frames

video_bp = Blueprint('video', __name__)

@video_bp.route('/feed', methods=['GET'])
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
