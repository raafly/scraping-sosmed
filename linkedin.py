from linkedin_api import Linkedin

def scrape_linkedin_profile(username: str, password: str, profile_url: str):
    """Scrape LinkedIn profile data."""
    try:
        # Login to LinkedIn
        api = Linkedin(username, password)
        
        # Extract profile ID from URL
        profile_id = profile_url.split('/')[-1]
        
        # Get profile data
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

# Contoh penggunaan
username = "your_linkedin_username"
password = "your_linkedin_password"
profile_url = "https://www.linkedin.com/rapitechindonesia/"
data = scrape_linkedin_profile(username, password, profile_url)
# print(data)