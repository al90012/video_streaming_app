from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configuration
app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://localhost:27017/video_stream_db")
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "default-secret-key")

# Initialize Extensions
CORS(app)
mongo = PyMongo(app)
jwt = JWTManager(app)

# Register Blueprints (Placeholder)
from routes.auth import auth_bp
from routes.dashboard import dashboard_bp
from routes.video import video_bp
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
app.register_blueprint(video_bp, url_prefix='/video')

@app.route('/')
def home():
    return jsonify({"message": "Video Streaming API is running"}), 200

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
