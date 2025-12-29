# Scraping Instagram with Python

import instaloader

# Create an instance of Instaloader
bot = instaloader.Instaloader()

# Load a profile from an Instagram handle
profile = instaloader.Profile.from_username(bot.context, 'aman.kharwal')

# Extract profile information
print("Username:", profile.username)
print("User ID:", profile.userid)
print("Number of Posts:", profile.mediacount)
print("Followers:", profile.followers)
print("Followees:", profile.followees)
print("Bio:", profile.biography, profile.external_url)

# Optional: Login to Instagram
# bot.login(user="your_username", passwd="your_password")
# or
# bot.interactive_login("your_username")

# Scraping followers and followees
followers = [f.username for f in profile.get_followers()]
followees = [f.username for f in profile.get_followees()]

print("Followers list:", followers)
