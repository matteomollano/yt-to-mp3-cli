# yt to mp3 cli

This project is a Python command line interface that allows you to download songs from YouTube. <br> <br>

## How it works:
- Downloads a YouTube video as an mp3 file using yt-dlp library
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

### Command Line Installation

#### MacOS
```bash
# Python
brew install python

# ffmpeg
brew install ffmpeg
```

#### Windows
```powershell
# Python
winget install -e --id Python.Python.3

# ffmpeg
winget install -e --id Gyan.FFmpeg
```

#### Linux
```bash
sudo apt install python3 ffmpeg
```
<br>

## How to use it:
1. Download the git repository using the following command <br>
```bash
git clone https://github.com/matteomollano/yt-to-mp3-cli.git
```

2. Navigate inside the project folder and create a virtual environment <br>
```bash
python3 -m venv .venv
```

3. You should now see a .venv directory in your project folder. Activate the virtual environment <br>
```bash
source .venv/bin/activate
```

4. Install the requirements <br>
```bash
pip3 install -r requirements.txt
```

5. Run main.py <br>
```bash
python3 main.py
```

6. Enter the YouTube URL, song title, and artist name for the song that you want to download <br>

    The song will now download as an mp3 in your Downloads folder!
