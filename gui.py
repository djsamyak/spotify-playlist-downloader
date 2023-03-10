import os
import app as base_runner

SPOTIPY_CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET')

SAVE_PATH = r"D:\Work\Programming\spotify-downloader\media"
FFMPEG_PATH = r"D:\Work\Programming\spotify-downloader\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe"

playlist_uri = "spotify:playlist:5KhLyV61d9KOmDLwEzJVlN"

downloader = base_runner.Spotify_Download(SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET)
downloader.set_playlist_uri(playlist_uri)
downloader.fetch_playlist_details()
downloader.download(SAVE_PATH,FFMPEG_PATH)