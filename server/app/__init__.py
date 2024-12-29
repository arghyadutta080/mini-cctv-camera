from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize extensions
    db.init_app(app)
    CORS(app)

    # Register blueprints
    from app.routes import video_bp, metadata_bp
    app.register_blueprint(video_bp, url_prefix='/video')
    app.register_blueprint(metadata_bp, url_prefix='/metadata')

    return app
