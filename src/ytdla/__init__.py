import sys
import os

def main():
    links = sys.argv[1:]
    if len(links) == 0:
        print('pass links to the script, like: ytdla "https://www.youtube.com/watch?v=TeSgUmh_7jc"')
    for link in links:
        cmd = "yt-dlp"
        cmd += " --no-playlist"
        cmd += " --extract-audio"
        cmd += " --audio-format mp3"
        cmd += " --embed-thumbnail"
        cmd += " --embed-metadata"
        cmd += " --embed-chapters"
        cmd += " --embed-info-json"
        cmd += " --format '251/140/bestaudio/mp3/91/best'"
        cmd += " --sponsorblock-remove all"
        cmd += " --age-limit 99"
        cmd += " --write-info-json"
        cmd += " --concurrent-fragments 12"
        cmd += " -o '%(channel,series,uploader,playlist_title,title)s - %(title)s.%(ext)s'"
        cmd += " '" + link + "'"

        os.system(cmd)
