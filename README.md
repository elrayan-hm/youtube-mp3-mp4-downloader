# YouTube Video Downloader (MP3 & MP4)
A Python-based tool that allows you to download YouTube videos in either MP3 (audio only) or MP4 (video) formats with a simple user interface. This tool leverages the powerful yt-dlp library to provide high-quality downloads, including the option to select your preferred format and resolution.

## Features
* MP3 Downloads: Extracts and downloads the best available audio in MP3 format.
* MP4 Downloads: Downloads the best available video (up to 1080p) in MP4 format.
* User-friendly: Simple command-line interface where users can input the video URL and choose the format they prefer.
* Optimized for High-Quality Downloads: The script ensures you get the best available quality based on your selected format.

## Requirements
* Python 3.6 or higher
* yt-dlp library for downloading videos and extracting audio
* Internet connection for downloading the content

## Installation
* Install dependencies: Ensure you have Python 3 installed. Then, install the required libraries using pip:
pip install yt-dlp

## Usage
Clone the repository and install the required dependencies.
* Run the script:
python ytb.py

When prompted, enter the URL of the YouTube video you want to download.

* Choose the format you'd like to download:

1. Enter 3 to download the audio as an **MP3 file**.
2. Enter 4 to download the video as an **MP4 file** (up to 1080p).
* The script will handle the rest, and once the download is complete, it will notify you with a success message.
