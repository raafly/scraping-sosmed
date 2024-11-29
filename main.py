from flask import Flask, request, jsonify
import instaloader
from linkedin_api import Linkedin
import yt_dlp

app = Flask(__name__)

# Instagram function
def get_instagram_data(username: str):
    loader = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        return {
            "followers": profile.followers,
        }
    except Exception as e:
        return {"error": f"Failed to fetch data for {username}: {str(e)}"}

# LinkedIn function
def get_linkedin_data(username: str, password: str, profile_url: str):
    try:
        api = Linkedin(username, password)
        profile_id = profile_url.split('/')[-1]
        profile = api.get_profile(profile_id)
        return {
            "first_name": profile.get('firstName'),
            "last_name": profile.get('lastName'),
            "headline": profile.get('headline'),
            "location": profile.get('locationName'),
            "industry": profile.get('industryName'),
            "summary": profile.get('summary'),
            "experience": profile.get('experience'),
            "education": profile.get('education'),
            "skills": profile.get('skills'),
            "connections": profile.get('numConnections'),
        }
    except Exception as e:
        return {"error": str(e)}

# YouTube function
def get_youtube_subscriber_count(url):
    ydl_opts = {
        'quiet': True,
        'extract_flat': 'in_playlist',
        'skip_download': True,
        'force_generic_extractor': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            subscriber_count = info.get("channel_follower_count")
            return {"subscribers": subscriber_count}
        except Exception as e:
            return {"error": str(e)}

@app.route('/sosmed', methods=['GET'])
def sosmed():
    instagram_username = 'rapiertechnology'
    youtube_url = 'https://www.youtube.com/@RapierTechnology'

    response = {
        "instagram": get_instagram_data(instagram_username),
        "youtube": get_youtube_subscriber_count(youtube_url)
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)