import yt_dlp
import asyncio

url = "https://www.youtube.com/@RapierTechnology"

ydl_opts = {
    'quiet': True,
    'extract_flat': 'in_playlist',
    'skip_download': True,
    'force_generic_extractor': True,  
}

def get_subscriber_count(url):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        subscriber_count = info.get("channel_follower_count")
        return subscriber_count

async def main():
    subscriber_count = get_subscriber_count(url)
    print(f"Jumlah Subscriber: {subscriber_count}")

if __name__ == "__main__":
    asyncio.run(main())