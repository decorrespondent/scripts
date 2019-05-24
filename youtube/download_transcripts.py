#This scripts takes the urls of YouTube videos and downloads the automatically created transcripts
#The files are saved in the folder where the script is executed
#The script uses the youtube-dl library

import youtube_dl

videos = [] # provide a list of videos


def get_captions(videos):
    ydl_opts = {
        'writeautomaticsub': True,
        'skip_download': True,
        'nocheckcertificate': True,

    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        for video in videos:
            try:
                ydl.download([video])
            except:
                continue

