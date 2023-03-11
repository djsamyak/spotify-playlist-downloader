import os
import app as backend

offset_counter = 0
playlist_uri = "spotify:playlist:74fyd8F4UMEzIXF5dlrWbV"

SPOTIPY_CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET')

SAVE_PATH = r"D:\Work\Programming\spotify-downloader\media"
FFMPEG_PATH = r"D:\Work\Programming\spotify-downloader\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe"

backend.importer([SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET,SAVE_PATH,FFMPEG_PATH])
backend.fetch_playlist_details(playlist_uri,offset_counter)
backend.download()