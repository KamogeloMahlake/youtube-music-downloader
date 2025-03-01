from pytubefix import YouTube, Playlist, Search
from pytubefix.cli import on_progress

def download_song(url=""):
    try:
        if not url:
            url = input("Enter url: \n>>")
        yt = YouTube(url, on_progress_callback=on_progress)

        audio = yt.streams.get_audio_only()

        audio.download("./music")
        print(f"{yt.title} has been downloaded")
    except Exception as e:
            return e
    return "done"

def download_playlist(url=""):
    try:
        if not url:
            url = input("Enter url: \n>>")
        pl = Playlist(url)
        for s in pl.videos:
            audio = s.streams.get_audio_only()
            audio.download("./music")
            print(f"{s.title} has been downloaded")

    except Exception as e:
        return e
    return "done"

def search():
    try:
        results = Search(input("Search: "))
        num = 0
        for video in results.videos:
            print(f"{num}. {video.title}")
            num += 1

        choice = int(input("Enter choice: \n>>"))
        download_song(results.videos[choice].watch_url)

    except Exception as e:
        return e
    return "done"

if __name__ == "__main__":
    while True:
        try:
            choice = int(input("1. Download Song\n2. Download Playlist\n3. Search \n>> "))
            if choice < 1 or choice > 3:
                print("Pick from the given menu")
                continue

            match choice:
                case 1:
                    print(download_song())
                case 2:
                    print(download_playlist())
                case 3:
                    print(search())
            break
        except Exception as e:
            print(e)
