import eyed3

def display_properties(filepath: str):
    audio_file = eyed3.load(filepath)
    print(f"Title: {audio_file.tag.title}")
    print(f"Artist: {audio_file.tag.artist}")
    print(f"Genre: {audio_file.tag.genre.name}")
    print(f"Album: {audio_file.tag.album}")
    
def update_properties(filepath: str, title: str, artist: str, genre: str, album: str):
    audio_file = eyed3.load(filepath)
    audio_file.tag.title = title
    audio_file.tag.artist = artist
    audio_file.tag.genre = genre
    audio_file.tag.album = album
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