import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import time

# Spotify setup
CLIENT_ID = "f7b2ec9ff2354c0986a83f49a8513f8f"
CLIENT_SECRET = "7c67ef85f01d49d5a18463526c9705d5"
REDIRECT_URI = "http://example.com"

os.environ['SPOTIPY_CLIENT_ID'] = CLIENT_ID
os.environ['SPOTIPY_CLIENT_SECRET'] = CLIENT_SECRET
os.environ['SPOTIPY_REDIRECT_URI'] = REDIRECT_URI

scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# Ask the user for the date
user_input = input("Which year do you want to travel to? YYYY-MM-DD: ")

# Build the Billboard URL
billboard_url = f"https://www.billboard.com/charts/hot-100/{user_input}"

# Scrape the data
response = requests.get(billboard_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the song titles on the page
song_elements = soup.find_all('h3', id="title-of-a-story", class_="a-no-trucate")
top_100_songs = [song.get_text(strip=True) for song in song_elements]

# Print the top 100 songs
print(f"Top 100 Songs on {user_input}:")
for i, song in enumerate(top_100_songs, 1):
    print(f"{i}. {song}")

# Create a new playlist
playlist_name = f"Billboard Top 100 - {user_input}"
playlist_description = f"Top 100 songs from Billboard Hot 100 on {user_input}."
playlist = sp.user_playlist_create(user=sp.current_user()['id'], name=playlist_name, public=False, description=playlist_description)

# Search and add songs to the playlist
track_uris = []
found_counter = 0
total_songs = len(top_100_songs)

for song in top_100_songs:
    try:
        # Search for the song on Spotify
        result = sp.search(q=song, type="track", limit=1)
        if result['tracks']['items']:
            track_uri = result['tracks']['items'][0]['uri']
            track_uris.append(track_uri)
            found_counter += 1
            print(f"Found {found_counter}/{total_songs}: {song}")
        else:
            print(f"Not Found: {song}")
    except Exception as e:
        print(f"Error searching for {song}: {e}")
    # To avoid hitting API rate limits
    time.sleep(0.5)

# Add the found songs to the playlist
if track_uris:
    sp.playlist_add_items(playlist_id=playlist['id'], items=track_uris)
    print(f"Added {len(track_uris)} songs to the playlist '{playlist_name}'.")

# Summary
print(f"Playlist '{playlist_name}' created successfully with {len(track_uris)} tracks.")
