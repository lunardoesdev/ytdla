
import sys
from yt_dlp import YoutubeDL


def main():
    links = sys.argv[1:]
    if not links:
        print('pass links to the script, like: ytdla "https://www.youtube.com/watch?v=TeSgUmh_7jc"')
        raise SystemExit(1)

    ydl_opts = {
        "ignoreconfig": True,
        "noplaylist": True,
        "format": "251/140/bestaudio/mp3/91/best",
        "outtmpl": "%(channel,series,uploader,playlist_title,title)s - %(title)s.%(ext)s",
        "age_limit": 99,
        "writethumbnail": True,
        "writeinfojson": True,
        "embedthumbnail": True,
        "addmetadata": True,
        "embedchapters": True,
        "sponsorblock_remove": ["all"],
        "concurrent_fragment_downloads": 12,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
            },
        ],
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(links)


if __name__ == "__main__":
    main()

