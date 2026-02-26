import os, yt_dlp, questionary
from metadata import add_artist
from album_art import download_thumbnail, add_thumbnail

def hook(d):
    if d['status'] == 'finished':
        print(f'\nDone downloading video: {d["filename"]}')

def download_song(url: str, title: str, artist: str):
    ydl_opts_mp3 = {
        'format': 'bestaudio/best', 
        # 'outtmpl': f'%(title)s.%(ext)s',
        'outtmpl': f'{title}.%(ext)s',
        'postprocessors': [{  # post-processing to convert to MP3
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '0', # highest quality
        }],
        'progress_hooks': [hook],  # optional: progress hooks for downloading status
    }
    
    # download the video and convert to MP3
    with yt_dlp.YoutubeDL(ydl_opts_mp3) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        uploader = info_dict.get("uploader", None)
        ydl.download([url])
    
    filepath = f"{title}.mp3"
    
    # add artist name to metadata
    if artist:
        add_artist(filepath=filepath, artist=artist)
    else:
        add_artist(filepath=filepath, artist=uploader)
    
    # add cover art
    choice = questionary.select(
        "Choose a cover art option:",
        choices=["YouTube Thumbnail", "No Cover Art"]
    ).ask()
    
    if choice == "YouTube Thumbnail":
        try:
            # download the video's thumbnail
            thumbnail_url = info_dict.get("thumbnail", None)
            download_thumbnail(thumbnail_url=thumbnail_url)
            # add the thumbnail as cover art to the mp3
            add_thumbnail(filename=filepath)
        except:
            print("Couldn't download video thumbnail from YouTube")
    else:
        print("Proceeding with no cover art...")
    
    # perform some file cleanup
    thumbnail_filepath = "thumbnail.jpg"
    square_thumbnail_filepath = "square_thumbnail.jpg"
    
    if os.path.exists(thumbnail_filepath):
        os.remove(thumbnail_filepath)
        
    if os.path.exists(square_thumbnail_filepath):
        os.remove(square_thumbnail_filepath)