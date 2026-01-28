from flask import Blueprint, jsonify, current_app
from flask_jwt_extended import jwt_required
from models.video import Video

dashboard_bp = Blueprint('dashboard', __name__)

def get_mongo():
    return current_app.extensions['pymongo']

@dashboard_bp.route('/', methods=['GET'])
@jwt_required()
def get_dashboard():
    mongo = get_mongo()
    videos = Video.get_active_videos(mongo)
    
    # Serialize ObjectId to string
    video_list = []
    for video in videos:
        video_curr = {
            'id': str(video['_id']),
            'title': video['title'],
            'thumbnail_url': video['thumbnail_url'],
            # Intentionally NOT returning youtube_id or is_active logic
        }
        video_list.append(video_curr)

    return jsonify(video_list), 200
