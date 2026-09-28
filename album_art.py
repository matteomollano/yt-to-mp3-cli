import eyed3, requests
from eyed3.id3.frames import ImageFrame

def download_thumbnail(thumbnail_url: str):
    """Downloads a youtube video's thumbnail as a jpg

    Args:
        thumbnail_url (str): a link to a youtube video's thumbnail
        Ex: https://i.ytimg.com/vi/{video_id}/maxresdefault.jpg
        where video_id is the ID string associated with a given youtube video

    Returns:
        str: path of the downloaded thumbnail file, or None if the download fails
    """

    thumbnail_path = "thumbnail.jpg"

    try:
        response = requests.get(thumbnail_url, timeout=30)
        response.raise_for_status()
        with open(thumbnail_path, "wb") as thumbnail_file:
            thumbnail_file.write(response.content)
    except Exception as e:
        print(f"Failed to download video thumbnail with error: {e}")
        return None

    return thumbnail_path


def add_thumbnail(mp3_path: str, thumbnail_path: str):
    """Adds YouTube thumbnail as cover art to an mp3 file

    Args:
        mp3_path (str): file path of the mp3 file
        thumbnail_path (str): file path of the youtube thumbnail jpg
    """

    try:
        audiofile = eyed3.load(mp3_path)

        if audiofile.tag is None:
            audiofile.initTag()

        with open(thumbnail_path, "rb") as img_file:
            audiofile.tag.images.set(
                ImageFrame.FRONT_COVER, # 3 is the code for front cover art
                img_file.read(),        # open the binary data of the cover art
                "image/jpeg"            # mime type of the file
            )

        audiofile.tag.save()
        print("Cover art added successfully")
    except Exception as error:
        print(f"Failed to add cover art: {error}")
