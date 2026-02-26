import eyed3

def display_properties(filepath: str):
    """Displays the metadata properties of an mp3 file

    Args:
        filepath (str): the filepath of the mp3 file
    """
    audio_file = eyed3.load(filepath)
    print(f"Title: {audio_file.tag.title}")
    print(f"Artist: {audio_file.tag.artist}")
    print(f"Album: {audio_file.tag.album}")
    print(f"Genre: {audio_file.tag.genre.name}")
    
    
def add_metadata(filepath: str, title: str, artist: str, genre: str, album: str):
    """Adds or updates metadata for an mp3 file

    Args:
        filepath (str): the filepath of the mp3 file
        title (str): the title to set
        artist (str): the artist to set
        genre (str): the genre to set
        album (str): the album to set
    """
    audio_file = eyed3.load(filepath)
    audio_file.tag.title = title
    audio_file.tag.artist = artist
    audio_file.tag.album = album
    audio_file.tag.genre = genre
    audio_file.tag.save()
    
    
def add_artist(filepath: str, artist: str):
    """Adds an artist name to an mp3's metadata

    Args:
        filepath (str): the filepath of the mp3 file
        artist (str): the artist name you want to add
    """
    audio_file = eyed3.load(filepath)
    audio_file.tag.artist = artist
    audio_file.tag.save()