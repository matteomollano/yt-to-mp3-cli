from download import downloadSong

if __name__ == '__main__':
 
    youtube_url = input("Enter YouTube URL for song download: ")
    song = input("Enter song name: ")
    artist = input("Enter artist name: ")
    
    downloadSong(youtube_url, song, artist)