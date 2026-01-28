from flask import Blueprint, jsonify, current_app, request
from flask_jwt_extended import jwt_required
from models.video import Video
from services.youtube_service import YouTubeService

video_bp = Blueprint('video', __name__)

def get_mongo():
    return current_app.extensions['pymongo']

@video_bp.route('/<video_id>/stream', methods=['GET'])
@jwt_required()
def get_video_stream(video_id):
    mongo = get_mongo()
    video = Video.get_video_by_id(mongo, video_id)
    
    if not video:
        return jsonify({"msg": "Video not found"}), 404

    if not video.get('is_active'):
         return jsonify({"msg": "Video is not available"}), 403
    
    stream_url = YouTubeService.get_stream_url(video['youtube_id'])
    
    if not stream_url:
        return jsonify({"msg": "Could not retrieve stream"}), 500

    return jsonify({
        "stream_url": stream_url,
        "masked": True 
    }), 200
