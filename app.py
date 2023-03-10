import re
import spotipy
import subprocess
from tqdm import tqdm
import urllib.request
from spotipy.oauth2 import SpotifyClientCredentials

# playlist_uri = "spotify:playlist:74fyd8F4UMEzIXF5dlrWbV"

class Spotify_Download():

    def __init__(self,SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET):

        self.offset_counter = 0
        self.playlist_tracks = []
        self.increment_counter = 0

        self.SPOTIPY_CLIENT_ID = SPOTIPY_CLIENT_ID
        self.SPOTIPY_CLIENT_SECRET = SPOTIPY_CLIENT_SECRET

        spotify = spotipy.Spotify(client_credentials_manager = SpotifyClientCredentials(self.SPOTIPY_CLIENT_ID,self.SPOTIPY_CLIENT_SECRET))

    def set_playlist_uri(self,playlist_uri):
        self.playlist_uri = playlist_uri
        
    def load_playlist_data(self,playlist_subsection_length,playlist_details):
        for _ in range(playlist_subsection_length):
            track_name = playlist_details['items'][_]['track']['name']
            track_artist = playlist_details['items'][_]['track']['artists'][0]['name']
            self.playlist_tracks.append([track_name,track_artist])

    def get_all_tracks(self,playlist_uri,offset=0):
        print(self.SPOTIPY_CLIENT_ID)
        print(self.SPOTIPY_CLIENT_SECRET)
        spotify = spotipy.Spotify(client_credentials_manager = SpotifyClientCredentials(self.SPOTIPY_CLIENT_ID,self.SPOTIPY_CLIENT_SECRET))
        playlist_details = spotify.playlist_items(playlist_uri,offset=offset)
        playlist_length = playlist_details['total'] - offset
        return playlist_length,playlist_details
    
    def fetch_playlist_details(self):
        playlist_length,playlist_details = self.get_all_tracks(self.playlist_uri)

        REQUIRED_INCREMENTS = playlist_length // 100

        if playlist_length > 100:
            if self.offset_counter == 0:
                self.load_playlist_data(100,playlist_details)
                self.offset_counter += 100 
                
            if self.offset_counter <= REQUIRED_INCREMENTS * 100:
                playlist_length,playlist_details = self.get_all_tracks(self.playlist_uri,self.offset_counter)
                self.load_playlist_data(playlist_length,playlist_details)
                self.offset_counter += 100 
        else:
            self.load_playlist_data(playlist_length,playlist_details)

    def download(self,SAVE_PATH,FFMPEG_PATH):
        for track_name,artist_name in tqdm(self.playlist_tracks):
            print(track_name)
            try:
                search_query1 = "+".join(str(track_name).split())
                search_query2 = "+".join(str(artist_name).split())

                html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={search_query1}+{search_query2}+lyrics")
                video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
                youtube_video_URL = "https://www.youtube.com/watch?v=" + video_ids[0]

                # print(track_name)
                # print(youtube_video_URL)

                AUDIO_SAVE_PATH = SAVE_PATH + f"\{track_name} - {artist_name}.%(ext)s"

                subprocess.run(['yt-dlp','-f','bestaudio', '--extract-audio', '--audio-format', 'mp3', '--audio-quality', '0','--quiet', '--ffmpeg-location', FFMPEG_PATH, '-o', AUDIO_SAVE_PATH, youtube_video_URL])
            
            except Exception as e:
                print(e)
                print("\n-----------------------------")
                print(search_query1)
                print(search_query2)
                print("-----------------------------\n")
