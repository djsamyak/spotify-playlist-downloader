import os
import app as backend

offset_counter = 0
# playlist_uri = "spotify:playlist:74fyd8F4UMEzIXF5dlrWbV"
# SAVE_PATH = r"D:\Work\Programming\spotify-downloader\media"
# FFMPEG_PATH = r"D:\Work\Programming\spotify-downloader\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe"

SPOTIPY_CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET')

playlist_uri = input("Enter Playlist URI\n")
SAVE_PATH = input("Enter Download Directory (Absolute Path)\n")
FFMPEG_PATH = input("Enter Absolute Path for FFMPEG executable\n")

backend.importer([SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET,SAVE_PATH,FFMPEG_PATH])
backend.fetch_playlist_details(playlist_uri,offset_counter)
backend.download()