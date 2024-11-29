import asyncio
import instaloader
from TikTokApi import TikTokApi
from linkedin_api import Linkedin
from pytube import YouTube


def instagram(username: str):
    """
    Ambil data followers dari profil Instagram.
    
    :param username: Username Instagram (string).
    :return: Data pengguna atau pesan error.
    """
    loader = instaloader.Instaloader()
    try:
        # Mengambil profil berdasarkan username
        profile = instaloader.Profile.from_username(loader.context, username)
        return {
            "username": profile.username,
            "followers": profile.followers,
            "full_name": profile.full_name,
            "biography": profile.biography,
            "is_verified": profile.is_verified,
        }
    except Exception as e:
        return {"error": f"Failed to fetch data for {username}: {str(e)}"}


async def main():
    instagram_username = "rapiertechnology"
    # Ambil data dari fungsi `instagram`
    instagram_data = instagram(instagram_username)
    # Cetak data yang diambil
    print("Instagram Data:", instagram_data)


# Memanggil main secara asinkron
if __name__ == "__main__":
    asyncio.run(main())




# if __name__ == "__main__":
#     asyncio.run(main())

# import yt_dlp

# url = "https://www.youtube.com/@RapierTechnology"

# ydl_opts = {
#     'quiet': True,
#     'extract_flat': 'in_playlist',
#     'skip_download': True,
#     'force_generic_extractor': True,  
# }

# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     info = ydl.extract_info(url, download=False)
#     subscriber_count = info.get("channel_follower_count")

#     print(f"Jumlah Subscriber: {subscriber_count}")