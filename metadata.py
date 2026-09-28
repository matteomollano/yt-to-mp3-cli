import eyed3

def display_properties(mp3_path: str):
    """Displays the metadata properties of an mp3 file

    Args:
        mp3_path (str): the file path of the mp3 file
    """
    try:
        audio_file = eyed3.load(mp3_path)
        print(f"Title: {audio_file.tag.title}")
        print(f"Artist: {audio_file.tag.artist}")
        print(f"Album: {audio_file.tag.album}")
        print(f"Genre: {audio_file.tag.genre.name}")
    except Exception as error:
        print(f"Failed to display audio properties: {error}")


def add_metadata(mp3_path: str, title: str, artist: str, genre: str, album: str):
    """Adds or updates metadata for an mp3 file

    Args:
        mp3_path (str): the file path of the mp3 file
        title (str): the title to set
        artist (str): the artist to set
        genre (str): the genre to set
        album (str): the album to set
    """
    try:
        audio_file = eyed3.load(mp3_path)

        if audio_file.tag is None:
            audio_file.initTag()

        audio_file.tag.title = title
        audio_file.tag.artist = artist
        audio_file.tag.album = album
        audio_file.tag.genre = genre
        audio_file.tag.save()
        print("Audio metadata updated successfully.")
    except Exception as error:
        print(f"Failed to add audio metadata: {error}")


def add_artist(mp3_path: str, artist: str):
    """Adds an artist name to an mp3's metadata

    Args:
        mp3_path (str): the file path of the mp3 file
        artist (str): the artist name you want to add
    """
    try:
        audio_file = eyed3.load(mp3_path)

        if audio_file.tag is None:
            audio_file.initTag()

        audio_file.tag.artist = artist
        audio_file.tag.save()
        print(f"Artist metadata added: {artist}")
    except Exception as error:
        print(f"Failed to add artist metadata: {error}")
