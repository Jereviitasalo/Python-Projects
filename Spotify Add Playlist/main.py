import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
load_dotenv()

CLIENT_ID = os.environ.get("client_id")
CLIENT_SECRET = os.environ.get("client_secret")

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private",
                                                    client_id=CLIENT_ID,
                                                    client_secret=CLIENT_SECRET,
                                                    redirect_uri="http://example.com",
                                                    cache_path="token.txt"))

date = input("which year's top 100 songs do you want to make a Spotify list? Type the date in this format YYYY-MM-DD: ")
year = date.split("-")[0]

# Creates a better looking date
new_date = ""
for i, element in enumerate(reversed(date.split("-"))):
    new_date += element
    if i < 2:
        new_date += "/"

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}/")
website = response.text

soup = BeautifulSoup(website, "html.parser")

titles = soup.select("li > ul > li > h3")
song_titles = [title.getText(strip=True) for title in titles]

# Creating a list of song uris
song_uris = []
for title in song_titles:
    try:
        song_uri = spotify.search(q=f"track:{title} year:{year}", type="track")["tracks"]["items"][0]["uri"]
    except IndexError:
        print("Couldn't find one song for this date.")
    else:
        song_uris.append(song_uri)

user = spotify.current_user()
user_id = user["id"]
playlist_name = f"Top 100 {new_date}"
playlist = spotify.user_playlist_create(user=user_id, name=playlist_name, public=False)
playlist_id = playlist["id"]

spotify.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=song_uris)