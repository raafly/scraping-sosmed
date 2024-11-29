from TikTokApi import TikTokApi
import asyncio

async def scrape_tiktok_followers(username: str):
    """Scrape TikTok user followers count."""
    try:
        api = TikTokApi()
        user = api.user(username=username)
        user_info = user.info()
        followers_count = user_info['stats']['followerCount']
        return {"username": username, "followers": followers_count}
    except Exception as e:
        return {"error": str(e)}

async def main():
    username = "rapiertechnology"
    data = await scrape_tiktok_followers(username)
    print(data)

if __name__ == "__main__":
    asyncio.run(main())