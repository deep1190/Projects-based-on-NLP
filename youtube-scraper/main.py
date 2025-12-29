# Scraping YouTube with Python

from pytube import YouTube

# Input YouTube video link
link = input("Enter Link of Youtube Video: ")
yt = YouTube(link)

# Extract video information
print("Title :", yt.title)
print("Views :", yt.views)
print("Duration :", yt.length)
print("Description :", yt.description)
print("Ratings :", yt.rating)

# Download video
stream = yt.streams.get_highest_resolution()
stream.download()
print("Download completed!!")
