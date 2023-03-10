
    for track_name,artist_name in tqdm(playlist_tracks):
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
