import os
import app as backend

SPOTIPY_CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET')

playlist_uri = input("Playlist URI\n")
print()
SAVE_PATH = input("Download Directory\n")
print()
FFMPEG_PATH = input("FFMPEG Executable\n")
print() 


if SPOTIPY_CLIENT_ID == None:
    SPOTIPY_CLIENT_ID = input("Enter Spotify Developer Client ID\n")
    print()

if SPOTIPY_CLIENT_SECRET == None:
    SPOTIPY_CLIENT_SECRET = input("Enter Spotify Developer Client Secret\n")
    print()


backend.importer([SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET,SAVE_PATH,FFMPEG_PATH])
backend.fetch_playlist_details(playlist_uri)
backend.download()