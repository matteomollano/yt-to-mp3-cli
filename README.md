# yt to mp3 cli

This project is a Python command line interface that allows you to download songs from YouTube. <br> <br>

## How it works:
- Downloads a YouTube video as an mp4 file
- Converts the mp4 to an mp3 file via ffmpeg
- Updates the mp3 with additional metadata including title, artist, and cover art
<br> <br>

## How to use it:
1. Download the git repository using the following command <br>
```
git clone https://github.com/matteomollano/yt-to-mp3-cli.git
```

2. Install the requirements <br>
```
pip3 install -r requirements.txt
```

3. Download ffmpeg
```
# Install via homebrew
brew install ffmpeg

OR

# Download a static binary from ffmpeg's website
https://www.ffmpeg.org/download.html
```

4. Run main.py <br>
```
python3 main.py
```

5. Enter the YouTube URL, song name, and artist name for the song that you want to download <br>
```
The song will now download as an mp3 in your current directory!
```