from pytube import YouTube
from AlbumArt import downloadThumbnail, addThumbnail, addCustomCoverArt
from metadata import add_artist
import ffmpeg, questionary, os

def downloadVideo(url: str, filename: str):
    """Downloads a youtube video as an mp4 file

    Args:
        url (str): a youtube video url
        filename (str): name that you want for the mp4
    """
    
    # Create a YouTube object to interact with
    yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
    
    # Get the yt video to download
    video = yt.streams.filter().first()
   
    # Download the video as mp4
    mp4_filename = filename + '.mp4'
    video.download(filename=mp4_filename)
    

def convertToMP3(filename: str):
    """Converts an mp4 file to an mp3 using ffmpeg

    Args:
        filename (str): filename/filepath of the mp4 to convert
    """
    
    input_file = ffmpeg.input(filename + '.mp4')
    output_file = ffmpeg.output(input_file, filename + '.mp3', q='0')
    ffmpeg.run(output_file)
    
    
def downloadSong(url:str, filename: str, artist: str):
    """Provides a command line interface for downloading a YouTube video as an mp3 file

    Args:
        url (str): a youtube video url
        filename (str): name that you want for the mp3 file
        artist (str): name of the song's artist
    """
    
    # Download the song as an mp4
    downloadVideo(url=url, filename=filename)
    
    # Convert the mp4 to an mp3
    convertToMP3(filename=filename)
    
    # Add artist name to metadata
    add_artist(filepath=f"{filename}.mp3", artist=artist)
    
    # Add cover art
    choice = questionary.select(
        "Do you want to use the youtube thumbnail, a custom cover art, or no cover art?",
        ["YouTube Thumbnail", "Custom Cover Art", "No Cover Art"]
    ).ask()
    
    if choice == "YouTube Thumbnail":
        # Download the video's thumbnail
        try:
            yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
            videoID = yt.video_id
            thumbnailUrl = f"https://img.youtube.com/vi/{videoID}/maxresdefault.jpg"
            downloadThumbnail(thumbnail_url=thumbnailUrl)
            
            # Add the thumbnail as cover art to the mp3
            mp3_filename = filename + '.mp3'
            addThumbnail(filename=mp3_filename)
        except:
            print("Couldn't download video thumbnail from YouTube")
    elif choice == "Custom Cover Art":
        try:
            art_filepath = input("Enter the filepath of your cover art: ")
            addCustomCoverArt(mp3_filename=filename, art_filename=art_filepath)
        except:
            print("Not a valid filepath for cover art")
    else:
        print("Proceeding with no cover art...")
        
    # Perform some file cleanup
    mp4_filepath = f"{filename}.mp4"
    thumbnail_filepath = "thumbnail.jpg"
    square_thumbnail_filepath = "square_thumbnail.jpg"
    
    if os.path.exists(mp4_filepath):
        os.remove(mp4_filepath)
        print(f"{mp4_filepath} has been deleted")
    
    if os.path.exists(thumbnail_filepath):
        os.remove(thumbnail_filepath)
        print(f"{thumbnail_filepath} has been deleted")
        
    if os.path.exists(square_thumbnail_filepath):
        os.remove(square_thumbnail_filepath)
        print(f"{square_thumbnail_filepath} has been deleted")