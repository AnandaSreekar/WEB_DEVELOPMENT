import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the YouTube channel's videos page
channel_url = "https://www.youtube.com/@wscubetech/videos"

# Send a GET request to the channel page
response = requests.get(channel_url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all video elements
    video_elements = soup.find_all('a', {'id': 'video-title'})

    # List to store video data
    videos_data = []

    # Extract video titles and URLs
    for video in video_elements:
        title = video.get('title')
        url = 'https://www.youtube.com' + video.get('href')
        videos_data.append({'Title': title, 'URL': url})

    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(videos_data)

    # Save DataFrame to Excel and CSV files
    df.to_excel("youtube_videos.xlsx", index=False)
    df.to_csv("youtube_videos.csv", index=False)

    print("Data has been saved to youtube_videos.xlsx and youtube_videos.csv")
else:
    print(f"Failed to retrieve data. HTTP Status Code: {response.status_code}")
