import os, yt_dlp
from utilities import sanitize_filename

def hook(d):
    """Progress hook for yt_dlp downloads

    Args:
        d (dict): download status dictionary from yt_dlp
    """
    if d["status"] == "finished":
        print(f"\nDone downloading video: {d['filename']}")


def fetch_song_metadata(youtube_url):
    """Fetches metadata for a YouTube URL, including:
        1. thumbnail URL
        2. video title
        3. artist/uploader (channel name)

    Args:
        youtube_url (str): The URL of the YouTube video to retrieve metadata for.

    Returns:
        dict[str, str]: Metadata dictionary containing the thumbnail URL,
        video title, artist/uploader, and a cover_art boolean flag.
    """
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "skip_download": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=False)

    return {
        "thumbnail": info.get("thumbnail"),
        "title": info.get("title"),
        "artist": info.get("uploader"),
        "cover_art": True,
    }


def download_song(youtube_url: str, title: str):
    """Downloads a YouTube video as an MP3 file to the ~/Downloads folder

    Args:
        youtube_url (str): The URL of the YouTube video to download
        title (str): The title to use for the MP3 file

    Returns:
        str: Full file path of the downloaded mp3 file
    """
    home_dir = os.path.expanduser("~")
    output_path = os.path.join(home_dir, "Downloads")

    sanitized_title = sanitize_filename(title)

    ydl_opts_mp3 = {
        "no_warnings": True,
        "format": "bestaudio/best",
        "outtmpl": f"{output_path}/{sanitized_title}.%(ext)s",
        "postprocessors": [{  # post-processing to convert to MP3
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "0", # highest quality
        }],
        "progress_hooks": [hook],  # optional: progress hooks for downloading status
    }

    # download the video and convert to MP3
    with yt_dlp.YoutubeDL(ydl_opts_mp3) as ydl:
        ydl.download([youtube_url])

    return os.path.join(output_path, f"{sanitized_title}.mp3")
