import urllib.request
import re
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

offset_counter = 0
playlist_tracks = []
increment_counter = 0
playlist_uri = "spotify:playlist:74fyd8F4UMEzIXF5dlrWbV"

def load_playlist_data(playlist_subsection_length,playlist_details):
    for _ in range(playlist_subsection_length):
        track_name = playlist_details['items'][_]['track']['name']
        track_artist = playlist_details['items'][_]['track']['artists'][0]['name']
        playlist_tracks.append([track_name,track_artist])

def get_all_tracks(playlist_uri,offset=0):
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials("b8cf655bffe2441d9b6fea50458a75cd",'57aaad2c618d4193868ff5d094fb8cdb'))
    playlist_details = spotify.playlist_items(playlist_uri,offset=offset)
    playlist_length = playlist_details['total'] - offset
    return playlist_length,playlist_details


playlist_length,playlist_details = get_all_tracks(playlist_uri)

REQUIRED_INCREMENTS = playlist_length // 100

if playlist_length > 100:
    if offset_counter == 0:
        load_playlist_data(100,playlist_details)
        offset_counter += 100 
        
    if offset_counter <= REQUIRED_INCREMENTS * 100:
        playlist_length,playlist_details = get_all_tracks(playlist_uri,offset_counter)
        load_playlist_data(playlist_length,playlist_details)
        offset_counter += 100 
else:
    load_playlist_data(playlist_length,playlist_details)

print(playlist_tracks)