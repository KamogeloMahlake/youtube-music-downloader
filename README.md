
# youtube-music-downloader

A web app to download YouTube videos or playlists as audio or video files. Built with Flask and pytubefix.

## Features

- Download individual YouTube videos as audio or video.
- Download entire YouTube playlists as audio.
- Simple search interface for finding YouTube videos.
- Web-based UI built with Flask and Bootstrap.

## How it Works

- **Home Page:** Enter a YouTube video or playlist URL. Choose to download as audio or video.
- **Search:** Use the search bar to find YouTube videos by keyword.
- **Download:** Downloads are handled in-browser and saved to a chosen directory.

## Key Endpoints (`app.py`)

- `/` — Home page. Enter URLs to download, or search.
- `/download` — Handles the actual download (audio/video) and saves to your chosen directory.
- `/playlisturl` — Retrieves all video titles in a playlist.
- `/search` — Searches YouTube via pytubefix and displays results.

## Installation

1. Clone this repo:
   ```
   git clone https://github.com/KamogeloMahlake/youtube-music-downloader.git
   cd youtube-music-downloader
   ```

2. Install requirements:
   ```
   pip install -r requirements.txt
   ```

3. Run the app:
   ```
   flask run
   ```

**Note:** Requires Python 3 and `tkinter` (for directory selection).

## Dependencies

- Flask
- pytubefix
- requests
- tkinter

## Usage

- Navigate to `http://127.0.0.1:5000/` in your browser.
- Enter a YouTube URL or search for videos.
- Choose audio/video and download.

## Project Structure

- `app.py` — Main Flask app, routes and logic.
- `helpers.py` — Helper functions for downloading and searching.
- `templates/` — Jinja2 HTML templates.
- `static/` — CSS & JS assets.
