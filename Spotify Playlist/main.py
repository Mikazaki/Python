import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


CLIENT_ID = "5f3b721581134bd4ab090b4e603664d1"
CLIENT_SECRET = "fadbc0db9bf84dd4be1698187c29f392"
REDIRECT_URI = "http://example.com"

date = input("What year do you want to travel to? Enter date in this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{date}/"


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               username="Fahim Kazi"))

user_id = sp.current_user()["id"]




response = requests.get(URL)

web = response.text
URI = []

soup = BeautifulSoup(web, 'html.parser')

tag = soup.select(selector='ul li h3')
name = [song.getText().strip() for song in tag]

songs = name[:100]

year = date.split("-")[0]
for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        URI.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


playlist_name = f"{date} Billboard 100"

playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)

sp.playlist_add_items(playlist_id=playlist['id'], items=URI)

print(URI)

