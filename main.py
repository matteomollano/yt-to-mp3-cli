from download import download_song

if __name__ == "__main__":
 
    youtube_url = input("Enter YouTube URL for song download: ")
    title = input("Enter song title: ")
    artist = input("Enter artist name: ")
    
    download_song(youtube_url, title, artist)