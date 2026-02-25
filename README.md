# yt to mp3 cli

This project is a Python command line interface that allows you to download songs from YouTube. <br> <br>

## How it works:
- Downloads a YouTube video as an mp4 file
- Converts the mp4 to an mp3 file via ffmpeg
- Updates the mp3 with additional metadata including title, artist, and cover art
<br> <br>

## Prerequisites
This application requires python3 and ffmpeg. <br>

### Manual Installation:
```
# Python Download
https://www.python.org/downloads/

# Download a static binary from ffmpeg's website, and add the binary to your path
https://www.ffmpeg.org/download.html
```

### Installation via Homebrew:
```
# Python
brew install python

# ffmpeg
brew install ffmpeg
```
<br>

## How to use it:
1. Download the git repository using the following command <br>
```
git clone https://github.com/matteomollano/yt-to-mp3-cli.git
```

2. Navigate inside the project folder and create a virtual environment <br>
```
python3 -m venv myenv
```

3. You should now see a myenv directory in your project folder. Activate the virtual environment <br>
```
source myenv/bin/activate
```

4. Install the requirements <br>
```
pip3 install -r requirements.txt
```

5. Run main.py <br>
```
python3 main.py
```

6. Enter the YouTube URL, song name, and artist name for the song that you want to download <br>
```
The song will now download as an mp3 in your current directory!
```
<br>