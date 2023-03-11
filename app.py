import re
import spotipy
import subprocess
import urllib.request
from spotipy.oauth2 import SpotifyClientCredentials

offset_counter = 0
playlist_tracks = []
increment_counter = 0

args = {}

def importer(arg_list):
    args['SPOTIPY_CLIENT_ID'] = arg_list[0]
    args['SPOTIPY_CLIENT_SECRET'] = arg_list[1]
    args['SAVE_PATH'] = arg_list[2]
    args['FFMPEG_PATH'] = arg_list[3]

def load_playlist_data(playlist_subsection_length,playlist_details):
    for _ in range(playlist_subsection_length):
        track_name = playlist_details['items'][_]['track']['name']
        track_artist = playlist_details['items'][_]['track']['artists'][0]['name']
        playlist_tracks.append([track_name,track_artist])

def get_all_tracks(playlist_uri,offset=0):
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(args['SPOTIPY_CLIENT_ID'],args['SPOTIPY_CLIENT_SECRET']))
    playlist_details = spotify.playlist_items(playlist_uri,offset=offset)
    playlist_length = playlist_details['total'] - offset
    return playlist_length,playlist_details


def fetch_playlist_details(playlist_uri,offset_counter):
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

# print("\nCurrently Downloading: ",playlist_details['name'],end="\n\n")

def download():
    for track_name,artist_name in playlist_tracks:
        try:
            search_query1 = "+".join(str(track_name).split())
            search_query2 = "+".join(str(artist_name).split())

            html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={search_query1}+{search_query2}+lyrics")
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            youtube_video_URL = "https://www.youtube.com/watch?v=" + video_ids[0]

            # print(track_name)
            print(youtube_video_URL)

            AUDIO_SAVE_PATH = args['SAVE_PATH'] + f"\{track_name} - {artist_name}.%(ext)s"

            subprocess.run(['yt-dlp','-f','bestaudio', '--extract-audio', '--audio-format', 'mp3', '--audio-quality', '0','--quiet', '--ffmpeg-location', args['FFMPEG_PATH'], '-o', AUDIO_SAVE_PATH, youtube_video_URL])
        
        except Exception as e:
            print(e)
            print("\n-----------------------------")
            print(search_query1)
            print(search_query2)
            print("-----------------------------\n")