import yt_dlp

class YouTubeService:
    @staticmethod
    def get_stream_url(youtube_id):
        # Construct YouTube URL
        youtube_url = f"https://www.youtube.com/watch?v={youtube_id}"
        
        ydl_opts = {
            'format': 'best', # Get best quality
            'quiet': True,
            'no_warnings': True,
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(youtube_url, download=False)
                # Return the direct streaming URL
                return info.get('url')
        except Exception as e:
            print(f"Error fetching stream URL: {e}")
            return None
