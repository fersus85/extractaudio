import moviepy.editor
from pathlib import Path
from pytube import YouTube


def download_yt(link):
    # Init link and stream
    yt = YouTube(link)
    # Choose which tag(format) you want
    stream = yt.streams.get_by_itag(17)
    # Downloading video from YouTube
    stream.download('source')
    # Loop for choice tag
    # print(stream.title[:34])
    # for tag in range(0, len(yt.streams)):
    #     print(yt.streams[tag])


def convert_to_mp3(file):
    # Convert mp4,3gpp -> mp3

    video_file = Path(f'source/{file}')
    #
    video = moviepy.editor.VideoFileClip(f'{video_file}')
    #
    audio = video.audio
    audio.write_audiofile(f'result/{video_file.stem}.mp3')




