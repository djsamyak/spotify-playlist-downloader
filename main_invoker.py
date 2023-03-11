import app as backend

offset_counter = 0
playlist_tracks = []
increment_counter = 0

playlist_uri = "spotify:playlist:74fyd8F4UMEzIXF5dlrWbV"

backend.fetch_playlist_details(playlist_uri,offset_counter)
backend.download()