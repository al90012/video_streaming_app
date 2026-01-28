from app import app, mongo
from models.video import Video

def seed_data():
    with app.app_context():
        # Clear existing videos
        mongo.db.videos.delete_many({})
        
        # Add 2 videos
        Video.create_video(
            mongo,
            title="Sintel - Third Open Movie by Blender Foundation",
            thumbnail_url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Sintel_poster.jpg/800px-Sintel_poster.jpg",
            youtube_id="0wwv1rD4eK0" # Sintel
        )
        
        Video.create_video(
            mongo,
            title="Big Buck Bunny",
            thumbnail_url="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Big_buck_bunny_poster_big.jpg/800px-Big_buck_bunny_poster_big.jpg",
            youtube_id="aqz-KE-bpKQ" # Big Buck Bunny
        )
        
        print("Database seeded with 2 videos.")

if __name__ == '__main__':
    seed_data()
