from download import fetch_song_metadata, download_song
from metadata import add_artist
from album_art import download_thumbnail, add_thumbnail
from utilities import get_input
import questionary, os

def main():
    youtube_url = input("Enter YouTube URL for song download: ")
    song_metadata = fetch_song_metadata(youtube_url)

    print(f"Thumbnail URL: {song_metadata['thumbnail']}")
    print(f"Title: {song_metadata['title']}")
    print(f"Artist: {song_metadata['artist']}\n")

    while True:
        choice = questionary.select(
            "What would you like to change?",
            choices=[
                "Cover Art",
                "Title",
                "Artist",
                "Done",
                "Quit",
            ]
        ).ask()

        if choice == "Cover Art":
            thumbnail_choice = questionary.select(
                "Choose a cover art option:",
                choices=["Keep YouTube Thumbnail", "No Cover Art"]
            ).ask()

            if thumbnail_choice == "No Cover Art":
                song_metadata["cover_art"] = False
            else:
                song_metadata["cover_art"] = True

        elif choice == "Title":
            title = get_input("Song title: ")
            song_metadata["title"] = title

        elif choice == "Artist":
            artist = get_input("Enter artist: ")
            song_metadata["artist"] = artist

        elif choice == "Done":
            print("Your choices:")
            if song_metadata["cover_art"]:
                print(f"Cover Art: {song_metadata['thumbnail']}")
            else:
                print("No Cover Art")
            print(f"Title: {song_metadata['title']}")
            print(f"Artist: {song_metadata['artist']}")

            confirm = questionary.select(
                "Download with these settings?",
                ["Yes", "No"]
            ).ask()

            if confirm == "Yes":
                break

        else:
            exit()

        print()

    # download song
    mp3_path = download_song(youtube_url, song_metadata["title"])

    # add artist name to mp3's metadata
    if song_metadata["artist"]:
        add_artist(mp3_path=mp3_path, artist=song_metadata["artist"])

    # add thumbnail as cover art to mp3
    thumbnail_path = None
    if song_metadata["cover_art"]:
        thumbnail_path = download_thumbnail(song_metadata["thumbnail"])

        if thumbnail_path:
            add_thumbnail(mp3_path=mp3_path, thumbnail_path=thumbnail_path)

    # perform some file cleanup
    if thumbnail_path and os.path.exists(thumbnail_path):
        os.remove(thumbnail_path)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nDownload cancelled.")
