from flask_pymongo import PyMongo
from bson.objectid import ObjectId

class Video:
    @staticmethod
    def get_active_videos(mongo):
        videos = mongo.db.videos
        # Strictly serve exactly 2 active videos
        return list(videos.find({'is_active': True}).limit(2))

    @staticmethod
    def get_video_by_id(mongo, video_id):
        videos = mongo.db.videos
        return videos.find_one({'_id': ObjectId(video_id)})

    @staticmethod
    def create_video(mongo, title, thumbnail_url, youtube_id, is_active=True):
        videos = mongo.db.videos
        video_id = videos.insert_one({
            'title': title,
            'thumbnail_url': thumbnail_url,
            'youtube_id': youtube_id,
            'is_active': is_active
        }).inserted_id
        return str(video_id)
